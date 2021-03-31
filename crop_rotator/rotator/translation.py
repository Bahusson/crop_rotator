from modeltranslation.translator import translator, TranslationOptions
from .models import (
    CropMix,
    Crop,
    CropFamily,
    CropDataSource,
    CropDataFamilySource,
    CropDataTagSource,
    CropTag,
 )
from core.snippets import all_names


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


class CropDataFamilySourceTranslate(TranslationOptions):
    fields = ()


translator.register(CropDataFamilySource, CropDataFamilySourceTranslate)


class CropDataTagSourceTranslate(TranslationOptions):
    fields = ()


translator.register(CropDataTagSource, CropDataTagSourceTranslate)


class CropTagTranslate(TranslationOptions):
    fields = ("name", "descr",)


translator.register(CropTag, CropTagTranslate)
