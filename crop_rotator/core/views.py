from django.shortcuts import render, redirect
from django.shortcuts import render, redirect, get_object_or_404 as G404
from crop_rotator.settings import LANGUAGES as L
from strona.models import (
    PageSkin as S,
    PageNames as P,
)
from .classes import (
    PageElement as pe,
    PageLoad,
)
from .snippets import flare
from .models import RotatorAdminPanel
from .forms import RotatorAdminPanelForm
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
    pe_element = pe(the_element_class)

    def dispatch(self, request, element_id, *args, **kwargs):
        self.the_element = self.pe_element.by_id(G404=G404, id=element_id)
        if self.the_element.family.is_family_slave:
            the_element_family = self.the_element.family.master_family
        else:
            the_element_family = self.the_element.family
        return super(CropAdmin, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        context = {
            "element": self.the_element,
        }
        pl = PageLoad(P, L)
        context_lazy = pl.lazy_context(skins=S, context=context)
        template = "core/edit_element_admin.html"
        return render(request, template, context_lazy)

    def post(self, request, *args, **kwargs):
        pass

# Edytuj
@method_decorator(staff_member_required, name="dispatch")
class FamilyAdmin(CropAdmin):
    the_element_class = CropFamily

    def dispatch(self, request, element_id, *args, **kwargs):
        self.the_element = self.pe_element.by_id(G404=G404, id=element_id)
        return super(CropAdmin, self).dispatch(request, *args, **kwargs)


@method_decorator(staff_member_required, name="dispatch")
class TagAdmin(CropAdmin):
    the_element_class = CropTag

    def dispatch(self, request, element_id, *args, **kwargs):
        self.the_element = self.pe_element.by_id(G404=G404, id=element_id)
        return super(CropAdmin, self).dispatch(request, *args, **kwargs)
