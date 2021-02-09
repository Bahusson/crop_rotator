from modeltranslation.translator import translator, TranslationOptions
from .models import (
    RotationPlan,
    RotationStep,
    CropMix,
    Crop,
    CropFamily,
    CropDataSource,
    CropTag,
 )
from core.snippets import all_names


class RotationPlanTranslate(TranslationOptions):
    fields = ("title",)


translator.register(RotationPlan, RotationPlanTranslate)


class RotationStepTranslate(TranslationOptions):
    fields = ("title", "descr",)


translator.register(RotationStep, RotationStepTranslate)


class CropMixTranslate(TranslationOptions):
    fields = ("name", "descr",)


translator.register(CropMix, CropMixTranslate)


class CropTranslate(TranslationOptions):
    fields = ("name", "descr",)


translator.register(Crop, CropTranslate)


class CropFamilyTranslate(TranslationOptions):
    fields = ("name",)


translator.register(CropFamily, CropFamilyTranslate)


class CropDataSourceTranslate(TranslationOptions):
    fields = ("descr",)


translator.register(CropDataSource, CropDataSourceTranslate)


class CropTagTranslate(TranslationOptions):
    fields = ("name", "descr",)


translator.register(CropTag, CropTagTranslate)
