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
from django.contrib.admin.views.decorators import staff_member_required

# Widok uproszczonego admina.
@staff_member_required
def rotator_admin(request):
    pe_rap = pe(RotatorAdminPanel).baseattrs
    context = {
        "admin_items": pe_rap,
    }

    pl = PageLoad(P, L)
    context_lazy = pl.lazy_context(skins=S, context=context)
    template = "core/rotator_admin.html"
    return render(request, template, context_lazy)
