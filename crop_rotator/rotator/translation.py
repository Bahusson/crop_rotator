from modeltranslation.translator import translator, TranslationOptions
from .models import (
    CropMix,
    MixCrop,
    Crop,
    CropFamily,
    CropDataSource,
    CropDataFamilySource,
    CropDataTagSource,
    CropTag,
 )


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


class MixCropTranslate(TranslationOptions):
    fields = ()


translator.register(MixCrop, MixCropTranslate)
