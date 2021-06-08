from django.shortcuts import render, get_object_or_404 as G404
from .models import (
    PageSkin as S,
    PageNames as P,
    AboutPageNames,
    RotatorEditorPageNames,
)
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rekruter.models import (
    RotationPlan,
    RotationStep,
    RotationSubStep,
)
from rotator.models import (
    Crop,
    CropFamily,
    CropDataSource as CDS,
    CropDataFamilySource as FDS,
    CropDataTagSource as TDS,
    CropTag,
    CropInteraction,
    CropBookString,
)
from crop_rotator.settings import LANGUAGES as L
from core.classes import (
    PageElement as pe,
    PageLoad,
#    count_sources_pages,

)
from core.snippets import (
    flare,
    check_slaves,
    slice_list_3,
    summarize_plans,
    list_crops_to,
    none_ify,
    remove_repeating,
)
from operator import attrgetter
from random import shuffle
from django.views import View
import copy

# Widok strony domowej.
def home(request):
    pe_rp_published = RotationPlan.objects.filter(published=True)
    pe_rp_shuffled = list(pe_rp_published)
    shuffle(pe_rp_shuffled)  # Losuje z widocznych na głównej.
    pe_rp_shuffled = pe_rp_shuffled[:4]
    plans_list = summarize_plans(pe_rp_shuffled, RotationStep, RotationSubStep)
    context = {
        "rotation_plans": plans_list,
    }
    pl = PageLoad(P, L)
    context_lazy = pl.lazy_context(skins=S, context=context)
    template = "strona/home.html"
    return render(request, template, context_lazy)


# Widok "O programie"
def about(request):
    pe_apn = pe(AboutPageNames).baseattrs
    # policz rodziny niebędące "slaves"
    crf = CropFamily.objects.filter(is_family_slave=False)
    num_families = len(crf)
    # policz wszystkie rośliny uprawne
    pe_c = pe(Crop).allelements
    num_crops = len(pe_c)
    # policz wszystkie kategorie
    pe_ctag = pe(CropTag).allelements
    num_categories = len(pe_ctag)
    # policz wszystkie interakcje
    pe_interact = pe(CropInteraction).allelements
    num_interactions = len(pe_interact)
    # policz wszystkie źródła
    pe_sources = pe(CropBookString).allelements
    num_sources = len(pe_sources)
    context = {
        "about_us": pe_apn,
        "num_families": num_families,
        "num_crops": num_crops,
        "num_categories": num_categories,
        "num_interactions": num_interactions,
        "num_sources": num_sources,
    }
    pl = PageLoad(P, L)
    context_lazy = pl.lazy_context(skins=S, context=context)
    template = "strona/about.html"
    return render(request, template, context_lazy)



# Widok "O źródłach"
def about_sources(request):
    pe_sources = pe(CropBookString).allelements
#    count_sources_pages(CDS)
    context = {
        "sources": pe_sources,
    }
    pl = PageLoad(P, L)
    context_lazy = pl.lazy_context(skins=S, context=context)
    template = "strona/about_sources.html"
    return render(request, template, context_lazy)


# Widok strony "O nawozach"
def fertilize(request):
    pe_apn = pe(AboutPageNames).baseattrs
    context = {
        "about_us": pe_apn,
    }
    pl = PageLoad(P, L)
    context_lazy = pl.lazy_context(skins=S, context=context)
    template = "strona/about.html"
    return render(request, template, context_lazy)


# Spis wszystkich rodzin, bez "nibyrodzin" (typu owies u wiechlinowatych).
class AllPlantFamilies(View):
    crf = CropFamily.objects.filter(is_family_slave=False)
    redirect_link = "family"
    template = "strona/all_plant_families.html"

    def get(self, request, *args, **kwargs):
        sl3 = slice_list_3(self.crf)
        context = {
            "redir": self.redirect_link,
            "families": self.crf,
            "ml1": sl3[0],
            "ml2": sl3[1],
        }
        pl = PageLoad(P, L)
        context_lazy = pl.lazy_context(skins=S, context=context)
        return render(request, self.template, context_lazy)


# Spis wszystkich tagów.
class AllTags(AllPlantFamilies):
    redirect_link = "tag"
    crf = CropTag.objects.all()


# Spis wszystkich roślin.
class AllCrops(AllPlantFamilies):
    redirect_link = "crop"
    crf = Crop.objects.all()


# Bazowy widok strony podglądu interakcji. Domyślnie wyświetla "Crop"
# TODO: Przywrócić do stanu, żeby było czytelne.
@method_decorator(cache_page(1), name='dispatch')
class InteractionPage(View):
    is_family = False
    is_tag = False
    base_item = Crop
    template = "strona/crop.html"

    def get(self, request, crop_id, *args, **kwargs):
        myitem = pe(self.base_item)
        house = []
        crop_family_from = []
        crop_family_to = []
        crop_tags_from = []
        crop_tags_to = []
        crop_from = []
        crop_to = []
        crop_to_new = []
        crop_family_to_new = []
        crop_tags_from_new = []
        crop_tags_to_new = []


        # Crop
        if not self.is_family and not self.is_tag:
            pe_c_id = myitem.by_id(G404=G404, id=crop_id)
            c_family = pe_c_id.family
            family_id = c_family.id
            crop_id = pe_c_id.id
            crop_from = none_ify(
             pe_c_id.crop_relationships.all().filter(
             is_server_generated=False).exclude(interaction_sign=0)
             )
            crop_to_c = Crop.objects.filter(
             crop_relationships__about_crop=crop_id,
             crop_relationships__is_server_generated=False,
             ).exclude(crop_relationships__interaction_sign=0)
            family_to_c = CropFamily.objects.filter(
             crop_relationships__about_crop=crop_id,
             crop_relationships__is_server_generated=False,
             ).exclude(crop_relationships__interaction_sign=0)
            tag_to_c = CropTag.objects.filter(
             crop_relationships__about_crop=crop_id,
             crop_relationships__is_server_generated=False,
             ).exclude(crop_relationships__interaction_sign=0)
            crop_to = list_crops_to(
             pe_c_id, crop_to_c, family_to_c, tag_to_c, "crop")
            remove_repeating(crop_to_new, crop_to)
            pe_cds = CDS.objects.filter(from_crop=crop_id)
            master_family = pe_c_id.family.name
            if pe_c_id.family.is_family_slave and not pe_c_id.is_fertilizer and not pe_c_id.is_crop_mix:
                master_family = pe_c_id.family.family_master.name


        # Family
        if self.is_family:
            family_id = crop_id
            c_family = myitem.by_id(G404=G404, id=family_id)
            c_family_sub = False

        # Crop, Family
        if not self.is_tag:
            crop_family_from = none_ify(c_family.crop_relationships.all())
            crop_to_f = Crop.objects.filter(
             crop_relationships__about_family=family_id,
             crop_relationships__is_server_generated=False,
            ).exclude(crop_relationships__interaction_sign=0)
            family_to_f = CropFamily.objects.filter(
             crop_relationships__about_family=family_id,
             crop_relationships__is_server_generated=False,
            ).exclude(crop_relationships__interaction_sign=0)
            tag_to_f = CropTag.objects.filter(
             crop_relationships__about_family=family_id,
             crop_relationships__is_server_generated=False,
            ).exclude(crop_relationships__interaction_sign=0)
            crop_family_to = list_crops_to(
             c_family, crop_to_f, family_to_f, tag_to_f, "family")
            remove_repeating(crop_family_to_new, crop_family_to)


        # Crop, Tag
        if self.is_family:
            if c_family.is_family_slave:
                sub_id = c_family.family_master.id
                c_family_sub = myitem.by_id(G404=G404, id=sub_id)
            family_slav_list = check_slaves(
                c_family,
                c_family_sub,
                c_family.is_family_slave,
            )
            pe_cds = FDS.objects.filter(from_family=family_id)
            pe_c_id = c_family
            for item in family_slav_list:
                pe_c_all = Crop.objects.filter(family=item.id)
                for crop_object in pe_c_all:
                    house.append(crop_object)
            master_family = family_slav_list[0]

        # Tag
        if self.is_tag:
            tag = myitem.by_id(G404=G404, id=crop_id)
            for relationship in tag.crop_relationships.all():
                crop_tags_from.append((tag, relationship))
            remove_repeating(crop_tags_from_new, crop_tags_from)
            crop_to_t = Crop.objects.filter(
             crop_relationships__about_tag=tag.id,
             crop_relationships__is_server_generated=False,
            ).exclude(crop_relationships__interaction_sign=0)
            family_to_t = CropFamily.objects.filter(
             crop_relationships__about_tag=tag.id,
             crop_relationships__is_server_generated=False,
            ).exclude(crop_relationships__interaction_sign=0)
            tag_to_t = CropTag.objects.filter(
             crop_relationships__about_tag=tag.id,
             crop_relationships__is_server_generated=False,
            ).exclude(crop_relationships__interaction_sign=0)
            crop_tags_to_0 = list_crops_to(
             tag, crop_to_t, family_to_t, tag_to_t, "tag")
            for item in crop_tags_to_0:
                crop_tags_to.append(item)
            remove_repeating(crop_tags_to_new, crop_tags_to)

            pe_cds = TDS.objects.filter(from_tag=crop_id)
            master_family = tag
            pe_c_id = tag
            family_slav_list = Crop.objects.filter(tags=tag.id)
            for item in family_slav_list:
                house.append(item)

        # Crop
        if not self.is_family and not self.is_tag:
            for tag in pe_c_id.tags.all():
                for relationship in tag.crop_relationships.all():
                    crop_tags_from.append((tag, relationship))
                remove_repeating(crop_tags_from_new, crop_tags_from)
                crop_to_t = Crop.objects.filter(
                 crop_relationships__about_tag=tag.id,
                 crop_relationships__is_server_generated=False,
                ).exclude(crop_relationships__interaction_sign=0)
                family_to_t = CropFamily.objects.filter(
                 crop_relationships__about_tag=tag.id,
                 crop_relationships__is_server_generated=False,
                ).exclude(crop_relationships__interaction_sign=0)
                tag_to_t = CropTag.objects.filter(
                 crop_relationships__about_tag=tag.id,
                 crop_relationships__is_server_generated=False,
                ).exclude(crop_relationships__interaction_sign=0)
                crop_tags_to_0 = list_crops_to(
                 tag, crop_to_t, family_to_t, tag_to_t, "tag")
                for item in crop_tags_to_0:
                    crop_tags_to.append(item)
                remove_repeating(crop_tags_to_new, crop_tags_to)

        house = sorted(house, key=attrgetter('name'))
        sl3 = slice_list_3(house)
        translatables = pe(RotatorEditorPageNames).baseattrs
        context = {
            "family": master_family,
            "crop": pe_c_id,
            "sources": pe_cds,
            "translatables": translatables,
            "crop_from": crop_from,
            "crop_to": crop_to_new,
            "house": house,
            "ml1": sl3[0],
            "ml2": sl3[1],
            "crop_family_from": crop_family_from,
            "crop_family_to": crop_family_to_new,
            "crop_tags_from": crop_tags_from_new,
            "crop_tags_to": crop_tags_to_new,
        }
        pl = PageLoad(P, L)
        context_lazy = pl.lazy_context(skins=S, context=context)
        return render(request, self.template, context_lazy)


# Widok podglądu interakcji dla danej rodziny.
@method_decorator(cache_page(360), name='dispatch')
class InteractionFamily(InteractionPage):
    is_family = True
    base_item = CropFamily
    template = "strona/family.html"


# Widok podglądu interakcji dla danego taga.
@method_decorator(cache_page(360), name='dispatch')
class InteractionTag(InteractionPage):
    is_tag = True
    base_item = CropTag
    template = "strona/family.html"
