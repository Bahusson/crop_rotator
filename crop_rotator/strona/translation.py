from modeltranslation.translator import translator, TranslationOptions
from strona.models import (
    PageNames,
    RegNames,
    AboutPageNames,
    RotatorEditorPageNames,
    FertilizerPageNames,
    BasicElement,
    Fertilizer,
    FertilizerDataSource,
    ElementDataString,
)
from core.snippets import all_names


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


class RotatorEditorPageNamesTranslate(TranslationOptions):
    allfields = all_names(RotatorEditorPageNames)
    fields = allfields


translator.register(RotatorEditorPageNames, RotatorEditorPageNamesTranslate)


class FertilizerPageNamesTranslate(TranslationOptions):
    allfields = all_names(FertilizerPageNames)
    fields = allfields


translator.register(FertilizerPageNames, FertilizerPageNamesTranslate)


class BasicElementTranslate(TranslationOptions):
    fields = ("name", "descr",)


translator.register(BasicElement, BasicElementTranslate)


class FertilizerTranslate(TranslationOptions):
    fields = ("name", "descr",)


translator.register(Fertilizer, FertilizerTranslate)


class FertilizerDataSourceTranslate(TranslationOptions):
    fields = ("title", "descr",)


translator.register(FertilizerDataSource, FertilizerDataSourceTranslate)


class ElementDataStringTranslate(TranslationOptions):
    fields = ("title", "part1", "link",)


translator.register(ElementDataString, ElementDataStringTranslate)
