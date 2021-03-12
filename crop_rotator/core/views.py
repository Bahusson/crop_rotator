from django.shortcuts import render
from strona.models import (
    PageSkin as S,
    PageNames as P,
)
from .classes import (
    PageElement as pe,
    PageLoad,
)
from . models import RotatorAdminPanel
from . forms import RotatorAdminPanelForm
from django.contrib.admin.views.decorators import staff_member_required

# Widok uproszczonego admina.
@staff_member_required
def rotator_admin(request):
    pe_rap = pe(RotatorAdminPanel).baseattrs
    if request.method == 'POST':
        form = RotatorAdminPanelForm(request.POST, instance=pe_rap)
        if form.is_valid():
            form.save()
            return redirect('rotator_admin') # Przekierowuj później na stronę planu
    else:
        form = RotatorAdminPanelForm(instance=pe_rap)
        context = {
            "admin_items": pe_rap,
        }
        form = Rotator
        pl = PageLoad(P, L)
        context_lazy = pl.lazy_context(skins=S, context=context)
        template = "core/rotator_admin.html"
        return render(request, template, context_lazy)
