from .snippets import (
    remove_repeating,
    flare,
    list_appending_long,
    level_off,
    )
import itertools
import copy
from core.models import RotatorAdminPanel


class PageLoad(object):
    """Zwraca tyle języków ile mamy zainstalowane
    w ustawieniach w zakładce LANGUAGES w formacie naprzemiennym
    pasującym do wzornika z dwoma wyjściowymi
    (ID_Języka, Ścieżka_Flagi_Języka), oraz
    Ładuje wszystkie podstawowe elementy w widoku strony."""

    def __init__(self, *args):
        lang_id = []
        langsl = []
        a = args[0]
        b = args[1]
        self.langs = []
        locations = list(a.objects.all())
        self.items = locations[0]
        for item in b:
            lang_id.append("lang_flag_" + str(item[0]))

        x = len(lang_id) - 1
        y = 0

        while x + 1 > 0:
            z = self.items.__dict__[lang_id[y]]
            langsl.append(z)
            x = x - 1
            y = y + 1

        self.langs = zip(lang_id, langsl)

    # Funkcji używaj jeśli chcesz używać zmiennych skórek.
    # Defaultuje do 0 jeśli nie wybierzesz żadnej.
    def page_dress(self, **kwargs):
        c = 0
        s = kwargs["skins"]
        if "choice" in kwargs:
            c = int(kwargs["choice"])
        self.skins = list(s.objects.all())
        self.skin = self.skins[c]
        self.skinctx = {
            "skin": self.skin,
        }
        return self.skinctx

    # Funkcja tworzy za nas podstawowy kontekst,
    # który rozszerza się o dany w funkcji.
    def lazy_context(self, **kwargs):
        self.context = {
            "items": self.items,
            "langs": self.langs,
        }
        if "skins" in kwargs:
            self.page_dress(**kwargs)
            self.context.update(self.skinctx)
        if "context" in kwargs:
            self.context.update(kwargs["context"])
        return self.context


# Nakładka na django do obsługi dodatku tłumaczeniowego django-modeltranslation.
class PageElement(object):
    def __init__(self, *args, **kwargs):
        self.x = args[0]
        self.listed = list(self.x.objects.all())  # Lista obiektów
        self.allelements = self.x.objects.all()  # Wszystkie obiekty
        self.elements = self.x.objects  # Obiekty
        self.baseattrs = self.listed[0]  # Pierwsze obiekty na liście

    # Konkretnte obiekty na liście (nie pierwsze).
    def list_specific(self, num):
        self.listed_specific = self.listed[num]
        return self.listed_specific

    # Obcina listę obiektów w konretnych miejscach.
    def list_shorter(self, **kwargs):
        if "cut_fr" in kwargs:
            cut_from = kwargs["cut_fr"]
        else:
            cut_to = None
        if "cut_to" in kwargs:
            cut_to = kwargs["cut_to"]
        else:
            cut_to = None
        cut_list = self.listed[cut_from:cut_to]
        return cut_list

    # Działa tylko jeśli wszystkie atrybuty są tłumaczone.
    # Zwraca gołe nazwy atrybutów bez względu na ilość języków.
    def get_attrnames(self, langs, cut_fr=2):
        preqlist = list(self.baseattrs.__dict__.keys())
        preqlist2 = preqlist[cut_fr:]  # Obetnij czołówkę.
        self.attrnames = preqlist2[0 :: len(langs) + 1]
        return self.attrnames

    # Zwraca pojedynczy przetłumaczony obiekt.
    def get_setter(self, place, quarter, langs, cut_fr=2):
        attrnames = self.get_attrnames(langs, cut_fr)
        attrobjects = self.list_specific(place)
        self.setter = attrobjects.__getattribute__(attrnames[int(quarter) - 1])
        return self.setter

    # Zwraca listę przetłumaczonych atrybutów
    def get_setlist(self, place, langs, cut_fr=2):
        attrnames = self.get_attrnames(langs, cut_fr)
        attrobjects = self.list_specific(place)
        self.setlist = []
        for item in attrnames:
            self.setlist.append(attrobjects.__getattribute__(item))
        return self.setlist

    # Elementy po Id.
    def by_id(self, **kwargs):
        G404 = kwargs["G404"]
        x_id = kwargs["id"]
        one_by_id = G404(self.x, pk=x_id)
        return one_by_id

    # lista integerów.
    def listedint(self):
        mylist = []
        for item in self.listed:
            mylist.append(int(item))
        return mylist


# Klasa ładuje stronę po dodaniu opcji typu panel admina.
class PortalLoad(PageLoad):
    def __init__(self, *args):
        super().__init__(*args)
        menus = args[2]
        advert = args[3]
        self.adverts = advert.objects.all()
        self.adverts_listed = list(advert.objects.all())
        self.menu = list(menus.objects.all())[0]
        if len(self.adverts_listed) == 0:
            self.adverts = False

    def page_dress(self, **kwargs):
        super().page_dress(**kwargs)

    def lazy_context(self, **kwargs):
        self.context = {
            "items": self.items,
            "langs": self.langs,
            "menu": self.menu,
            "adverts": self.adverts,
        }
        if "skins" in kwargs:
            self.page_dress(**kwargs)
            self.context.update(self.skinctx)
        if "context" in kwargs:
            self.context.update(kwargs["context"])
        return self.context


# Klasa liczy interakcje w crop plannerze - (klasa-slave)
class PlannerRelationship(object):
    def __init__(self, *args, **kwargs):
        self.top_tier = kwargs['top_tier']
        self.a = kwargs['a']
        self.b = kwargs['b']
        self.ifdict = {
            "crop_to_crop": self.a[4].crop_relationships.filter(
             about_crop__id=self.b[4].id),
            "crop_to_family": self.a[4].crop_relationships.filter(
             about_family__id=self.b[4].family.id),
            "family_to_crop": self.a[4].family.crop_relationships.filter(
             about_crop__id=self.b[4].id),
            "family_to_family": self.a[4].family.crop_relationships.filter(
             about_family__id=self.b[4].family.id),
        }
        self.seasondict = {
            0: None,
            1: "Summer",
            2: "Winter",
        }

    def finishing(self, **kwargs):
        interactiondict = {
         0: [0, 0],  # Współrzędne
         1: [0, 1],  # Allelopatyczne / Współrzędne i następcze
         2: [1, 1],  # Następcze
         3: [2, 2],  # W drugim roku
         4: [3, 3],  # W trzecim roku
         5: [1, 2],  # W pierwszym i drugim roku
         }
        self.given_list = kwargs['given_list']
        season = self.seasondict[self.i.season_of_interaction]
        if season == "Summer" or season is None:
            if (
                self.a[3][1] == self.b[3][1] - interactiondict[self.i.type_of_interaction][0]
                or self.a[3][1] == self.b[3][1] - interactiondict[self.i.type_of_interaction][1]
                 ):
                level_off(self.top_tier, self.a, self.b)
                self.given_list.append(self.a + self.b + [self.i.is_positive])
                return self.given_list

    def relationship(self, **kwargs):
        if self.ifdict[kwargs['relationship']].exists():
            for self.i in self.ifdict[kwargs['relationship']]:
                self.finishing(given_list=kwargs['given_list'])
                return self.given_list


# Klasa obchodzi błędy związane z używaniem wzornika
# CropPlanner tam gdzie nie potrzeba analizować treści.
class DummyCropPlanner(object):
    def __init__(self, *args, **kwargs):
        plan_id = kwargs['plan_id']
        self.pe_rp_id = args[0]
        self.pe_rs = args[1].objects.filter(from_plan=plan_id)
        self.pe_rss = args[3].objects.filter(from_step__from_plan=plan_id)
        err_crop_list = []
        tabs = []
        self.error_family_crops = {
            "e_crops": err_crop_list,
            "e_tabs": tabs,
        }
        listed_pe_rs = list(self.pe_rs)
        top_tier_list = []
        for item in listed_pe_rs:
            top_tier_list.append(item.order)
        top_tier_list.sort()
        self.top_tier = top_tier_list[-1]

    def basic_context(self, **kwargs):
        self.context = {
            "efcs": self.error_family_crops,
            "plan": self.pe_rp_id,
            "steps": self.pe_rs,
            "substeps": self.pe_rss,
            "top_tier": self.top_tier,
        }
        self.context.update(kwargs['context'])
        return self.context

    def top_tier(self):
        return self.top_tier


# Klasa analizuje płodozmian pod kątem błędów i synergii.
class CropPlanner(object):
    def __init__(self, *args, **kwargs):
        plan_id = kwargs['plan_id']
        self.pe_rp_id = args[0]
        self.pe_rs = args[1].objects.filter(from_plan=plan_id)
        self.pe_rss = args[3].objects.filter(from_step__from_plan=plan_id)
        rss_object = args[3]
        listed_pe_rs = list(self.pe_rs)
        len_listed_pe_rs = len(listed_pe_rs)
        cooldown_list = []
        fabacae = []
        top_tier_list = []
        sub_index = 0
        for item in listed_pe_rs:
            pe_rss_pack = args[3].objects.filter(from_step=item)
            rss_list = []
            for sub_item in pe_rss_pack:
                rss_list.append(sub_item)
            i4 = item.order
            top_tier_list.append(i4)
            vars = [cooldown_list, item, fabacae, sub_index]
            sub_index = list_appending_long(rss_list, vars, rss_object)
        cooldown_list.sort()
        top_tier_list.sort()
        self.clw = False
        error_len_crops = []
        cooldown_list1 = copy.deepcopy(cooldown_list)
        self.top_tier = top_tier_list[-1]
        for item in cooldown_list1:
            item[3][0] += self.top_tier
        cooldown_list2 = cooldown_list + cooldown_list1
        err_tab_list = []
        err_crop_list = []
        crop_interaction_list = []
        family_interaction_list = []
        crop_interaction_list_f = []
        family_interaction_list_f = []
        for item in cooldown_list:
            if item[0] > len_listed_pe_rs:
                error_len_crops.append(item[1])
                self.clw = args[2].objects.filter(id__in=error_len_crops)
        if not self.clw:
            for a, b in itertools.permutations(cooldown_list2, 2):  # permutacje
                if a[2] == b[2] and a[3][0] - b[3][0] < a[0] and a[3][0] - b[3][0] > 0:
                    level_off(self.top_tier, a, b)
                    err_tab_list.append(a[3][0])
                    err_tab_list.append(b[3][0])
                    err_crop_list.append(a + b)
                    err_crop_list.append(b + a)
                pr = PlannerRelationship(top_tier=self.top_tier, a=a, b=b)
                pr.relationship(
                 given_list=crop_interaction_list,
                 relationship="crop_to_crop")
                pr.relationship(
                 given_list=family_interaction_list,
                 relationship="crop_to_family")
                pr.relationship(
                 given_list=crop_interaction_list_f,
                 relationship="family_to_crop")
                pr.relationship(
                 given_list=family_interaction_list_f,
                 relationship="family_to_family")

        fabs = []
        tabs = []
        self.interactions = []
        self.interactions_f = []
        self.f_interactions = []
        self.f_interactions_f = []
        remove_repeating(fabs, fabacae)
        remove_repeating(tabs, err_tab_list)
        remove_repeating(self.interactions, crop_interaction_list)
        remove_repeating(self.interactions_f, family_interaction_list)
        remove_repeating(self.f_interactions, crop_interaction_list_f)
        remove_repeating(self.f_interactions_f, family_interaction_list_f)
        fabs_percent = float(len(fabs)) / float(self.top_tier * 3)
        fabs_rounded = round(fabs_percent, 3)
        self.fabs_error = False
        if fabs_rounded >= 0.25 and fabs_rounded <= 0.33:
            pass
        else:
            self.fabs_error = int(fabs_rounded * 100)
            self.fabs_error = str(self.fabs_error) + "%"
        self.error_family_crops = {
            "e_crops": err_crop_list,
            "e_tabs": tabs,
        }

    def basic_context(self, **kwargs):
        self.context = {
            "interactions": self.interactions,
            "interactions_f": self.interactions_f,
            "f_interactions": self.f_interactions,
            "f_interactions_f": self.f_interactions_f,
            "f_error": self.fabs_error,
            "efcs": self.error_family_crops,
            "cr_len_warning": self.clw,
            "plan": self.pe_rp_id,
            "steps": self.pe_rs,
            "substeps": self.pe_rss,
            "top_tier": self.top_tier,
        }
        self.context.update(kwargs['context'])
        return self.context

    def top_tier(self):
        return self.top_tier


# Do ładowania po raz pierwszy na serwer.
try:
    edit_delay_sec = PageElement(RotatorAdminPanel).baseattrs.evaluated_plan_cooldown
    lurk_delay_min = PageElement(RotatorAdminPanel).baseattrs.lurk_plan_cooldown
except:
    edit_delay_sec = 60
    lurk_delay_min = 15
