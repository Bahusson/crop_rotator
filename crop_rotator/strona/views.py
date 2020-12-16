from django.shortcuts import (render, redirect, get_object_or_404 as G404)
from django.contrib.auth.models import User  # Zaimportuj uproszczony model usera.
from .models import (PageSkin as S,  PageNames as P, RegNames)
from rotator.models import (RotationPlan)
from crop_rotator.settings import LANGUAGES as L
from meetap.core.classes import (PageElement as pe, PageLoad)

# Create your views here.

def home(request):
    context = {
     'rotation_plans': RotationPlan,
     }
    pl = PageLoad(P, L)
    context_lazy = pl.lazy_context(
     skins=S, context=context)
    template = 'strona/home.html'
    return render(request, template, context_lazy)
