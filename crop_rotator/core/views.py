from django.shortcuts import render, redirect
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
    ChangeElementCropsInteractionsForm,
    ChangeElementFamilyInteractionsForm,
    )
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from strona.views import AllPlantFamilies
from rotator.models import Crop, CropFamily, CropTag
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
    translatables = pe(RotatorEditorPageNames).baseattrs
    taglist = CropTag.objects.all()

    def dispatch(self, request, element_id, *args, **kwargs):
        self.element_id = element_id
        pe_element = pe(self.the_element_class)
        self.the_element = pe_element.by_id(G404=G404, id=element_id)
        if self.the_element_class == Crop:
            if self.the_element.family.is_family_slave:
                the_element_family = self.the_element.family.master_family
            else:
                the_element_family = self.the_element.family
        return super(CropAdmin, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        context = {
            "element": self.the_element,
            "translatables": self.translatables,
            "taglist": self.taglist,
        }
        pl = PageLoad(P, L)
        context_lazy = pl.lazy_context(skins=S, context=context)
        template = "core/edit_element_admin.html"
        return render(request, template, context_lazy)

    def post(self, request, *args, **kwargs):
        if "add_element_button" in request.POST:
            element_to_add = request.POST.get('add_element')
            pe_croptag_id = pe(CropTag).by_id(G404=G404, id=element_to_add)
            for item in pe_croptag_id:
                form = ChangeElementCropsInteractionsForm(id=pe_croptag_id)


            self.the_element.tags.add(element_to_add)
        if "remove_element_button" in request.POST:
            element_to_remove = request.POST.get('remove_element')
        #    for item in self.the_element.tags



        return redirect('crop_admin', self.element_id)

# Edytuj
@method_decorator(staff_member_required, name="dispatch")
class FamilyAdmin(CropAdmin):
    the_element_class = CropFamily


@method_decorator(staff_member_required, name="dispatch")
class TagAdmin(CropAdmin):
    the_element_class = CropTag
