from django.shortcuts import render, redirect, get_object_or_404 as G404
from crop_rotator.settings import LANGUAGES as L
from strona.models import (
    PageSkin as S,
    PageNames as P,
    RotatorEditorPageNames,
)
from .classes import (
    PageElement as pe,
    PageLoad,
)
from .snippets import flare
from .models import RotatorAdminPanel
from .forms import (
    RotatorAdminPanelForm,
    )
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from strona.views import AllPlantFamilies
from rotator.models import Crop, CropFamily, CropTag, CropsInteraction, CropInteraction
from django.views import View


# Widok uproszczonego admina.
@staff_member_required
def rotator_admin(request):
    pe_rap = pe(RotatorAdminPanel).baseattrs
    if request.method == 'POST':
        form = RotatorAdminPanelForm(request.POST, instance=pe_rap)
        if form.is_valid():
            form.save()
            return redirect('rotator_admin')
    else:
        form = RotatorAdminPanelForm(instance=pe_rap)
        context = {
            "form": form,
        }
        pl = PageLoad(P, L)
        context_lazy = pl.lazy_context(skins=S, context=context)
        template = "core/rotator_admin.html"
        return render(request, template, context_lazy)


# Wszystkie Rośliny do edycji.
@method_decorator(staff_member_required, name="dispatch")
class AllCropsAdmin(AllPlantFamilies):
    crf = Crop.objects.all()
    redirect_link = "crop_admin"
    template = "core/all_elements_admin.html"


# Wszystkie Rodziny do edycji.
@method_decorator(staff_member_required, name="dispatch")
class AllFamiliesAdmin(AllPlantFamilies):
    crf = CropFamily.objects.all()
    redirect_link = "family_admin"
    template = "core/all_elements_admin.html"


# Wszystkie tagi do edycji.
@method_decorator(staff_member_required, name="dispatch")
class AllTagsAdmin(AllPlantFamilies):
    redirect_link = "tag_admin"
    crf = CropTag.objects.all()
    template = "core/all_elements_admin.html"


@method_decorator(staff_member_required, name="dispatch")
class CropAdmin(View):
    the_element_class = Crop
    try:
        translatables = pe(RotatorEditorPageNames).baseattrs
    except:
        pass
    taglist = CropTag.objects.all()
    template = "core/edit_element_admin.html"

    def dispatch(self, request, element_id, *args, **kwargs):
        self.element_id = element_id
        pe_element = pe(self.the_element_class)
        self.the_element = pe_element.by_id(G404=G404, id=element_id)
        if self.the_element_class == Crop:
            if self.the_element.family.is_family_slave:
                self.the_element_family = self.the_element.family.master_family
        return super(CropAdmin, self).dispatch(request, *args, **kwargs)

    def add_element(
         self, query, element_to_add, *args):
        if args:
            self.the_element = args[0]
        pe_croptag_id = pe(CropTag).by_id(G404=G404, id=element_to_add)
        for item in query:
            for interaction in item.crop_relationships.all():
                if interaction.about_tag == pe_croptag_id:
                    self.add_common(
                     interaction, item, pe_croptag_id, item.id,
                     self.the_element.id, self.the_element, "add_element",
                     )
        self.the_element.tags.add(element_to_add)

    def add_family_element(
         self, query, element_to_add, *args):
        if args:
            self.the_element = args[0]
        pe_croptag_id = pe(CropTag).by_id(G404=G404, id=element_to_add)
        for item in query:
            for interaction in item.family.crop_relationships.all().filter(
             about_crop=self.the_element):
                for crop_item in Crop.objects.filter(family=item.family):
                    self.add_common(
                     interaction, item, pe_croptag_id, crop_item.id,
                     self.the_element.id, self.the_element,
                     "add_family_element"
                     )
        self.the_element.tags.add(element_to_add)

    def add_tag_element(
         self, query, element_to_add, *args):
        if args:
            self.the_element = args[0]
        pe_croptag_id = pe(CropTag).by_id(G404=G404, id=element_to_add)
        tags_searched = CropTag.objects.filter(
         crop_relationships__about_tag=pe_croptag_id,
         crop_relationships__is_server_generated=False)
        for item in query:
            for tag in item.tags.all():
                if tag in tags_searched:
                    for interaction in tag.crop_relationships.all():
                        self.add_common(
                         interaction, item, pe_croptag_id, item.id,
                         self.the_element.id, self.the_element,
                         "add_tag_element",
                         )
        self.the_element.tags.add(element_to_add)

    def add_tag_crop_element(
         self, element_to_add, *args):
        if args:
            self.the_element = args[0]
        pe_croptag_id = pe(CropTag).by_id(G404=G404, id=element_to_add)
        for interaction in pe_croptag_id.crop_relationships.all():
            if interaction.about_crop is not None:
                tag_type = interaction.about_crop
                self.add_common(
                 interaction, self.the_element, pe_croptag_id,
                 self.the_element.id, tag_type.id, interaction.about_crop,
                 "add_tag_crop_element",
                 )
            elif interaction.about_family is not None:
                for crop_item in Crop.objects.filter(
                 family=interaction.about_family.id):
                    tag_type = crop_item
                    self.add_common(
                     interaction, self.the_element, pe_croptag_id,
                     self.the_element.id, tag_type.id, interaction.about_crop,
                     "add_tag_crop_element",
                     )
            elif interaction.about_tag is not None:
                query = Crop.objects.filter(tags=interaction.about_tag.id)
                for item in query:
                    self.add_common(
                         interaction, self.the_element, pe_croptag_id,
                         self.the_element.id, item.id, item,
                         "add_tag_crop_element",
                          )
                self.the_element.tags.add(element_to_add)
            else:  # Jeśli tag też pusty śmigaj dalej.
                # TODO: Zapisz ID pustej interakcji do dziennika błędów.
                continue
        self.the_element.tags.add(element_to_add)

    def add_mass_family_to(self, *args):
        if args:
            self.the_element = args[0]
        for interaction in self.the_element.crop_relationships.all().exclude(
         about_family=None):
            flare(interaction)
            for crop_item in Crop.objects.filter(
             family=interaction.about_family.id):
                self.add_common(
                 interaction, self.the_element, None,
                 self.the_element.id, crop_item.id, interaction.about_crop,
                 "add_to_family",
                 )

    def add_mass_family_from(self, *args):
        if args:
            self.the_element = args[0]
        query = Crop.objects.filter(
         crop_relationships__about_family=self.the_element.family,
         crop_relationships__is_server_generated=False)
        for item in query:
            for interaction in item.crop_relationships.all().filter(
             about_family=self.the_element.family):
                for crop_item in Crop.objects.filter(family=item.family):
                    self.add_common(
                     interaction, item, None, crop_item.id,
                     self.the_element.id, self.the_element,
                     "add_from_family"
                     )

    def add_common(
         self, interaction, item, pe_croptag_id, item1, item2, about_crop, debug):
        if item1 != item2:
            signature = str(item1) + " " + str(item2) + " (" + str(interaction.type_of_interaction) + ")(" + str(interaction.season_of_interaction) + ")"
            if not CropsInteraction.objects.filter(signature=signature).exists():
                cr = CropsInteraction.create(
                     title=signature,
                     signature=signature,
                     is_positive=interaction.is_positive, # obsolete
                     interaction_sign=interaction.interaction_sign,
                     about_crop=about_crop,
                     about_family=None,
                     about_tag=None,
                     info_source=interaction.info_source,
                     type_of_interaction=interaction.type_of_interaction,
                     season_interaction=interaction.season_of_interaction,
                     is_server_generated=True,
                     server_interaction=interaction,
                     debug_line=debug,
                     trigger_crop=self.the_element,
                     trigger_tag=pe_croptag_id,
                     )
                cr.save()
                item.crop_relationships.add(cr.id)

    def map_all_properties(self, element):
        element_list = []
        element_list.append("c" + str(element.id))
        element_list.append("f" + str(element.family.id))
        for tag in element.tags.all():
            element_list.append("t" + str(tag.id))
        listToStr = ','.join([str(elem) for elem in element_list])
        element.meta_tags_source = listToStr
        element.save()

    def make_signatures(self, item):
        if item.about_crop:
            the_crop = Crop.objects.filter(crop_relationships=item)
            new_crop = the_crop[0].id
            item.signature = str(new_crop) + " " + str(item.about_crop.id) + " (" + str(item.type_of_interaction) + ")(" + str(item.season_of_interaction) + ")"
            item.save()

    #def rewrite_all_signs(self,item):
    #    signaturedict={True:2, False:1}
    #    item.interaction_sign = signaturedict[item.is_positive]
    #    item.save()

    def get(self, request, *args, **kwargs):
        context = {
            "element": self.the_element,
            "translatables": self.translatables,
            "taglist": self.taglist,
        }
        pl = PageLoad(P, L)
        context_lazy = pl.lazy_context(skins=S, context=context)
        return render(request, self.template, context_lazy)

    def post(self, request, *args, **kwargs):
        if "add_element_button" in request.POST:
            element_to_add = request.POST.get('add_element')
            crops_to_tag = Crop.objects.filter(
             crop_relationships__about_tag=element_to_add,
             crop_relationships__is_server_generated=False)
            family_to_tag = Crop.objects.filter(
             family__crop_relationships__about_tag=element_to_add,
             family__crop_relationships__is_server_generated=False)
            tag_to_tag = Crop.objects.filter(
             tags__crop_relationships__about_tag=element_to_add,
             tags__crop_relationships__is_server_generated=False)
            self.add_element(crops_to_tag, element_to_add)
            self.add_family_element(family_to_tag, element_to_add)
            self.add_tag_element(tag_to_tag, element_to_add)
            self.add_tag_crop_element(element_to_add)

        if "remove_element_button" in request.POST:
            element_to_remove = request.POST.get('remove_element')
            pe_croptag_id = pe(CropTag).by_id(G404=G404, id=element_to_remove)
            filter_cr1 = CropsInteraction.objects.filter(
             trigger_crop=self.the_element.id, trigger_tag=element_to_remove, )
            for interaction in filter_cr1:
                if interaction.is_server_generated:
                    interaction.delete()
            for interaction in self.the_element.crop_relationships.all():
                if interaction.about_tag == pe_croptag_id and interaction.is_server_generated:
                    interaction.delete()
            self.the_element.tags.remove(element_to_remove)
        return redirect('crop_admin', self.element_id)


@method_decorator(staff_member_required, name="dispatch")
class FamilyAdmin(CropAdmin):
    the_element_class = CropFamily


@method_decorator(staff_member_required, name="dispatch")
class TagAdmin(CropAdmin):
    the_element_class = CropTag


# Synchronizuj bazę danych tagów jednym kliknięciem.
@method_decorator(user_passes_test(lambda u: u.is_superuser), name="dispatch")
class SyncCropTagDB(CropAdmin):
    template = "core/admin_db_superpowers.html"

    def dispatch(self, request, *args, **kwargs):
        pass
        return super(CropAdmin, self).dispatch(request, *args, **kwargs)

    # Stwórz automatycznie  wszystkie (brakujące) dowiązania tagów.
    # Może trochę potrwać.
    def post(self, request, *args, **kwargs):
        if "populate_tag_db" in request.POST:
            query = Crop.objects.all()
            for crop in query:
                # Najpierw dowiąż zależności rodzin.
                self.add_mass_family_to(crop)
                self.add_mass_family_from(crop)
                # Potem dowiąż zależności tagów.
                for tag in crop.tags.all():
                    element_to_add = tag.id
                    crops_to_tag = Crop.objects.filter(
                     crop_relationships__about_tag=element_to_add,
                     crop_relationships__is_server_generated=False)
                    family_to_tag = Crop.objects.filter(
                     family__crop_relationships__about_tag=element_to_add,
                     family__crop_relationships__is_server_generated=False)
                    tag_to_tag = Crop.objects.filter(
                     tags__crop_relationships__about_tag=element_to_add,
                     tags__crop_relationships__is_server_generated=False)
                    self.add_element(
                     crops_to_tag, element_to_add, crop)
                    self.add_family_element(
                     family_to_tag, element_to_add, crop)
                    self.add_tag_element(
                     tag_to_tag, element_to_add, crop)
                    self.add_tag_crop_element(
                     element_to_add, crop)

        # Wywal wszystkie tagi stworzone maszynowo.
        if "purge_tag_db" in request.POST:
            query = CropsInteraction.objects.filter(is_server_generated=True)
            for item in query:
                item.delete()

        if "create_meta_tag_db" in request.POST:
            query = Crop.objects.filter(is_crop_mix=False)
            for crop in query:
                self.map_all_properties(crop)

        if "create_all_signatures_db" in request.POST:
            query = CropsInteraction.objects.filter(is_server_generated=False)
            for item in query:
        #        self.rewrite_all_signs(item)
                self.make_signatures(item)



        return redirect('rotator_admin')

    def get(self, request, *args, **kwargs):
        context = {
            "translatables": self.translatables,
            "taglist": self.taglist,
        }
        pl = PageLoad(P, L)
        context_lazy = pl.lazy_context(skins=S, context=context)
        return render(request, self.template, context_lazy)
