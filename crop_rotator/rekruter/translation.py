from modeltranslation.translator import translator, TranslationOptions
from .models import (
    RotationPlan,
    RotationStep,
)

class RotationPlanTranslate(TranslationOptions):
    fields = ("title",)


translator.register(RotationPlan, RotationPlanTranslate)


class RotationStepTranslate(TranslationOptions):
    fields = ("title", "descr",)


translator.register(RotationStep, RotationStepTranslate)
