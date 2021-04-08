from django.shortcuts import render, redirect
from crop_rotator.settings import LANGUAGES as L
from strona.models import (
    PageSkin as S,
    PageNames as P,
)
from .classes import (
    PageElement as pe,
    PageLoad,
)
from .models import RotatorAdminPanel
from .forms import RotatorAdminPanelForm
from django.contrib.admin.views.decorators import staff_member_required
from strona.views import AllPlantFamilies

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

@staff_member_required
class AllElementsAdmin(AllPlantFamilies):
    pass
