# from .snippets import flare


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
