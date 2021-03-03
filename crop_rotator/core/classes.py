from .snippets import (
    remove_repeating,
    flare,
#    list_appending_short,
    list_appending_long,
    level_off,
    )
import itertools
import copy

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

    # Funkcja tworzy za nas podstwwowy kontekst,
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


# Klasa ładowania widoków /strony/
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


class PartyMaster(object):
    # Podstawka zwraca wszystkie akcje kwaterunkowe
    def __init__(self, *args):
        H_Party = args[0]
        py_tz = args[1]
        dt = args[2]
        self.all_parties = PageElement(H_Party)
        tz_UTC = py_tz.timezone("Europe/Warsaw")
        self.dt_now = dt.datetime.now(tz_UTC)
        self.list_parties = self.all_parties.listed

    # Zwraca wszystkie akcje bez względu na czas serwera (atrybuty)
    def full_party(self, **kwargs):
        full_parties = []
        attrname = kwargs["attrname"]
        x = 0
        for item in self.list_parties:
            full_parties.append(str(self.list_parties[x].__dict__[attrname]))
            x = x + 1
        return full_parties

    # Zwraca tylko aktywne akcje względem czasu serwera (atrybuty)
    def active_party(self, **kwargs):
        active_parties = []
        attrname = kwargs["attrname"]
        x = 0
        for item in self.list_parties:
            if (
                self.list_parties[x].__dict__["date_start"]
                <= self.dt_now
                <= self.list_parties[x].__dict__["date_end"]
            ):
                active_parties.append(str(self.list_parties[x].__dict__[attrname]))
            x = x + 1
        return active_parties

    # Zwraca słownik z kqaterami przyporządkowanymi do ID
    def dict_active_id_quarter(self):
        active_quarters = []
        active_ids = []
        x = 0
        for item in self.list_parties:
            if (
                self.list_parties[x].__dict__["date_start"]
                <= self.dt_now
                <= self.list_parties[x].__dict__["date_end"]
            ):
                active_quarters.append(str(self.list_parties[x].__dict__["quarter"]))
                active_ids.append(str(self.list_parties[x].__dict__["id"]))
            x = x + 1
        active_parties = dict(zip(active_ids, active_quarters))
        return active_parties

    # Tylko nieaktywne akcje względem czasu serwera (atrybuty)
    def past_party(self, **kwargs):
        inactive_parties = []
        attrname = kwargs["attrname"]
        date_end = "date_end"
        if "date_end" in kwargs:
            date_end = kwargs["date_end"]
        x = 0
        for item in self.list_parties:
            if self.list_parties[x].__dict__[date_end] < self.dt_now:
                inactive_parties.append(str(self.list_parties[x].__dict__[attrname]))
            x = x + 1
        return inactive_parties

    # Tylko zaplanowane akcje względem czasu serwera (atrybuty)
    def future_party(self, **kwargs):
        future_parties = []
        date_start = "date_start"
        attrname = kwargs["attrname"]
        if "date_start" in kwargs:
            date_start = kwargs["date_start"]
        x = 0
        for item in self.list_parties:
            if self.list_parties[x].__dict__[date_start] > self.dt_now:
                future_parties.append(str(self.list_parties[x].__dict__[attrname]))
            x = x + 1
        return future_parties


class AllParties(object):
    def __init__(self, request, *args, **kwargs):
        HParty = args[0]
        pytz = args[1]
        datetime = args[2]
        FormItems = args[3]
        Hpi = args[4]
        QuarterClassB = args[5]
        view_filter = kwargs["view_filter"]
        pm = PartyMaster(HParty, pytz, datetime)
        all_parties = pm.all_parties
        range = {
            "1": pm.full_party(attrname="id"),
            "2": pm.active_party(attrname="id"),
            "3": pm.past_party(attrname="id"),
            "4": pm.future_party(attrname="id"),
        }
        active_parties = []
        for item in range[view_filter]:
            obj = all_parties.elements.get(pk=item)
            active_parties.append(obj)
        pe_fi = PageElement(FormItems)
        all_parties = PageElement(HParty)
        hpi = PageElement(Hpi)
        peqc = PageElement(QuarterClassB)
        self.context = {
            "formitem": pe_fi.baseattrs,
            "parties": active_parties,
            "p_item": hpi.baseattrs,
            "setter": peqc.listed,
            "view_filter": view_filter,
        }


class ActivePageItems(object):
    def __init__(self, request, *args, **kwargs):
        Item = args[0]
        pytz = args[1]
        datetime = args[2]
        pm = PartyMaster(Item, pytz, datetime)
        all_items = pm.all_parties
        irange = pm.past_party(attrname="id", date_end="pubdate")
        self.active_items = []
        for item in irange:
            obj = all_items.elements.get(pk=item)
            self.active_items.append(obj)


def checkifnull(x, y):
    if x == "":
        return y
    elif x is None:
        return y
    else:
        return x

class PlannerRelationship(object):
    def __init__(self, *args, **kwargs):
        self.top_tier = kwargs['top_tier']
        self.a = kwargs['a']
        self.b = kwargs['b']
        self.ifdict = {
            # relationships:
            "crop_to_crop": self.a[4].crop_relationships.filter(about_crop__id=self.b[4].id),
            "crop_to_family": self.a[4].crop_relationships.filter(about_family__id=self.b[4].family.id),
            "family_to_crop": self.a[4].family.family_relationships.filter(about_crop__id=self.b[4].id),
            "family_to_family": self.a[4].family.family_relationships.filter(about_family__id=self.b[4].family.id),
            # tag_relationships:
            "crop_to_tag": [self.b[4].tags.all(), self.a[4].crop_relationships],
            "family_to_tag": [self.b[4].tags.all(), self.a[4].family.family_relationships],
        }
        self.seasondict = {
            0: None,
            1: True,
            2: False,
        }
    def finishing(self, **kwargs):
        interactiondict = {0: [0,0], 1: [0,1], 2: [1,1],}
        self.given_list = kwargs['given_list']
        season = self.seasondict[self.i.season_of_interaction]
        is_odd = self.b[3][1] % 2 != 0
        if season is is_odd or season is None:
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

    def tag_relationship(self, **kwargs):
        for tag in self.ifdict[kwargs['relationship']][0]:
            if self.ifdict[kwargs['relationship']][1].filter(about_tag__id=tag.id).exists():
                for self.i in self.ifdict[kwargs['relationship']][1].filter(about_tag__id=tag.id):
                    self.finishing(given_list=kwargs['given_list'])
                    return self.given_list

    # Wszystko co jest .all() jest zasobożerne.
    # Dawaj .exist() jeśli się da, bo to tylko jedno zapytanie zamiast łażenia po pętli.
    # A jak już dajesz 2xall, to szykuj się, że będzie mulić do kwadratu...
    # Do optymalizacji - jeśli to w ogóle możliwe - patrz: odłożone karty na GLO['interakcje'].
    def reverse_tag_relationship(self, **kwargs):
        for tag in self.a[4].tags.all():
            for self.i in tag.crop_relationships.all():
                self.tag_dict = {
                    "tag_to_crop": [self.i.about_crop, self.b[4]],
                    "tag_to_family": [self.i.about_family, self.b[4].family],
                }
                if self.tag_dict[kwargs['relationship']][0] == self.tag_dict[kwargs['relationship']][1]:
                    self.finishing(given_list=kwargs['given_list'])
                    return self.given_list

    # Nie testowałem taga do tagu (zatem pewnie nie działa :P), bo to będzie potencjalnie nieracjonalnie zasobożerne i na razie nie znalazłem zastosowania...
    # Jak znajdę to zrobię i wprowadzę. W ogóle to powinien być jakiś przełącznik na to wszystko czy coś... :]
    def tag_to_tag_relationship(self, **kwargs):
        for tag in self.a[4].tags.all():
            for tag2 in tag.crop_relationships.all():
                for tag3 in self.b[4].tags.all():
                    for self.i in tag3.crop_ralationships.all():
                        if self.i.about_tag == tag2.about_tag:
                            self.finishing(given_list=kwargs['given_list'])
                            return self.given_list


class DummyCropPlanner(object):
    def __init__(self, *args, **kwargs):
        plan_id = kwargs['plan_id']
        self.pe_rp_id = args[0]
        self.pe_rs = args[1].objects.filter(from_plan=plan_id)
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
            "top_tier": self.top_tier,
        }
        self.context.update(kwargs['context'])
        return self.context

    def top_tier(self):
        return self.top_tier

class CropPlanner(object):
    def __init__(self, *args, **kwargs):
        plan_id = kwargs['plan_id']
        self.pe_rp_id = args[0]
        self.pe_rs = args[1].objects.filter(from_plan=plan_id)
        listed_pe_rs = list(self.pe_rs)
        flare(listed_pe_rs)
        len_listed_pe_rs = len(listed_pe_rs)
        cooldown_list = []
        fabacae = []
        top_tier_list = []
        self.fertilized = True
        index = 0
        for item in listed_pe_rs:
            i1 = (list(item.early_crop.all()), item.order)
            flare(i1)
            i2 = (list(item.middle_crop.all()), item.order)
            i3 = (list(item.late_crop.all()), item.order)
            i4 = item.order
            if item.add_manure_early or item.add_manure_late or item.add_manure_middle:
                self.fertilized = False
            top_tier_list.append(i4)
            vars = [cooldown_list, item, fabacae, index]
    #        list_appending_short(i1, "a", vars)
    #        list_appending_short(i2, "b", vars)
    #        list_appending_short(i3, "c", vars)
            list_appending_long(i1,i2,i3,vars)
        cooldown_list.sort()
        #flare(cooldown_list)
        top_tier_list.sort()
        self.clw = False
        error_len_crops = []
        cooldown_list1 = copy.deepcopy(cooldown_list)  # kopiowanie listy
        self.top_tier = top_tier_list[-1]
        for item in cooldown_list1:
            item[3][0] += self.top_tier
        cooldown_list2 = cooldown_list + cooldown_list1
        err_tab_list = []
        err_crop_list = []
        crop_interaction_list = []
        family_interaction_list = []
        tag_interaction_list = []
        crop_interaction_list_f = []
        family_interaction_list_f = []
        tag_interaction_list_f = []
        crop_interaction_list_t = []
        family_interaction_list_t = []
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
                pr.relationship(given_list=crop_interaction_list, relationship="crop_to_crop")
                pr.relationship(given_list=family_interaction_list, relationship="crop_to_family")
                pr.relationship(given_list=crop_interaction_list_f, relationship="family_to_crop")
                pr.relationship(given_list=family_interaction_list_f, relationship="family_to_family")
                pr.tag_relationship(given_list=tag_interaction_list, relationship="crop_to_tag")
                pr.tag_relationship(given_list=tag_interaction_list_f, relationship="family_to_tag")
                pr.reverse_tag_relationship(given_list=crop_interaction_list_t, relationship="tag_to_crop")
                pr.reverse_tag_relationship(given_list=family_interaction_list_t, relationship="tag_to_family")
        fabs = []
        tabs = []
        self.interactions = []
        self.interactions_f = []
        self.f_interactions = []
        self.f_interactions_f = []
        self.interactions_t = []
        self.f_interactions_t = []
        self.t_interactions = []
        self.t_interactions_f = []
        remove_repeating(fabs, fabacae)
        remove_repeating(tabs, err_tab_list)
        remove_repeating(self.interactions, crop_interaction_list)
        remove_repeating(self.interactions_f, family_interaction_list)
        remove_repeating(self.f_interactions, crop_interaction_list_f)
        remove_repeating(self.f_interactions_f, family_interaction_list_f)
        remove_repeating(self.interactions_t, tag_interaction_list)
        remove_repeating(self.f_interactions_t, tag_interaction_list_f)
        remove_repeating(self.t_interactions, crop_interaction_list_t)
        remove_repeating(self.t_interactions_f, family_interaction_list_t)
        fabs_percent = float(len(fabs)) / float(self.top_tier * 2)
        fabs_rounded = round(fabs_percent, 2)
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
            "interactions_t": self.interactions_t,
            "f_interactions_t": self.f_interactions_t,
            "t_interactions": self.t_interactions,
            "t_interactions_f": self.t_interactions_f,
            "f_error": self.fabs_error,
            "efcs": self.error_family_crops,
            "cr_len_warning": self.clw,
            "plan": self.pe_rp_id,
            "steps": self.pe_rs,
            "top_tier": self.top_tier,
            "fertilized": self.fertilized,
        }
        self.context.update(kwargs['context'])
        return self.context

    def top_tier(self):
        return self.top_tier
