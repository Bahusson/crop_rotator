from modeltranslation.translator import translator, TranslationOptions
from strona.models import (PageNames, RegNames, AboutPageNames)
from crop_rotator.core.snippets import all_names


class PageNamesTranslate(TranslationOptions):
    allfields = all_names(PageNames)
    fields = allfields


translator.register(PageNames, PageNamesTranslate)


class RegNamesTranslate(TranslationOptions):
    allfields = all_names(RegNames)
    fields = allfields


translator.register(RegNames, RegNamesTranslate)


class AboutPageNamesTranslate(TranslationOptions):
    allfields = all_names(AboutPageNames)
    fields = allfields


translator.register(AboutPageNames, AboutPageNamesTranslate)
