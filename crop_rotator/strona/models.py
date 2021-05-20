from django.db import models


# Klasa tłumaczeniowa dla "core"
class PageNames(models.Model):
    lang_flag = models.ImageField(upload_to='images')  # Mały obrazek języka
    lang_flag_id = models.CharField(max_length=20, blank=True, null=True)
    headtitle = models.CharField(max_length=200)  # Nagłówek strony w tym j
    mainpage = models.CharField(max_length=200)  # Strona główna w tym języku
    all_plants = models.CharField(max_length=200, blank=True, null=True) # Spis roślin
    about = models.CharField(max_length=200)  # Informacje w tym języku
    contact = models.CharField(max_length=200)  # Kontakty w tym języku
    logout = models.CharField(max_length=200)  # Wyloguj
    login = models.CharField(max_length=200)  # zaloguj
    register = models.CharField(max_length=50)
    see_more = models.CharField(max_length=200)
    my_plans = models.CharField(max_length=200, blank=True, null=True) # Spis roślin
    all_plans = models.CharField(max_length=200, blank=True, null=True) # Wszystkie plany
    see_more = models.CharField(max_length=200, blank=True, null=True) # Czytaj dalej
    of_steps = models.CharField(max_length=200, blank=True, null=True) # Kroków
    of_plants = models.CharField(max_length=200, blank=True, null=True) # Czytaj dalej
    by_crops = models.CharField(max_length=50, blank=True, null=True) # Rośliny (button)
    by_families = models.CharField(max_length=50, blank=True, null=True) # Rodziny (button)
    by_tags = models.CharField(max_length=50, blank=True, null=True) # Kategorie (button)


    class Meta:
        verbose_name_plural = 'Page Names'


# Klasa tłumaczeniowa dla Login/Register i myprofile.
class RegNames(models.Model):
    password = models.CharField(max_length=50, blank=True, null=True)
    re_password = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    refresh = models.CharField(max_length=50, blank=True, null=True)
    passwd_too_simple = models.CharField(max_length=250, blank=True, null=True)
    register = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Registry Names'


# Klasa skórek do naszej apki. Pola nienulowalne.
class PageSkin(models.Model):
    themetitle = models.CharField(max_length=200)
    position = models.IntegerField()
    planimagedefault = models.ImageField(
     upload_to='skins', blank=True, null=True)
    rotatorlogo_main = models.ImageField(
     upload_to='skins', blank=True, null=True)

    class Meta:
        ordering = ['position']
        verbose_name_plural = 'Page Skins'

    def __str__(self):
        return self.themetitle


# klasa tłumaczeniowa dla strony "o projekcie"
class AboutPageNames(models.Model):
    about_project = models.TextField()  # Pole tekstowe dla strony about.
    send_email = models.CharField(max_length=200)  # Wyślij email
    gitter = models.CharField(max_length=200)  # Adres gittera
    github = models.CharField(max_length=200)  # Adres github
    login_to_see = models.CharField(max_length=200)  # zaloguj się by przeglądać
    curr_prog_includes = models.CharField(max_length=40, blank=True, null=True)  # Obecnie program zawiera bazę
    over = models.CharField(max_length=30, blank=True, null=True)  # Ponad
    plants = models.CharField(max_length=30, blank=True, null=True)  # roślin_uprawnych
    coming_from = models.CharField(max_length=30, blank=True, null=True)  # pochodzących z
    families = models.CharField(max_length=30, blank=True, null=True)  # rodzin
    marked_by = models.CharField(max_length=30, blank=True, null=True)  # oznaczonych według
    categories = models.CharField(max_length=30, blank=True, null=True)  # kategorii
    and_over = models.CharField(max_length=30, blank=True, null=True)  # i ponad
    unique_interactions = models.CharField(max_length=30, blank=True, null=True)  # unikalnych interakcji
    described_by = models.CharField(max_length=30, blank=True, null=True)  # opisanych na podstawie
    sources = models.CharField(max_length=30, blank=True, null=True)  # źródeł

    class Meta:
        verbose_name_plural = 'About Page Names'


# klasa tłumaczeniowa dla strony edycji planów.
class RotatorEditorPageNames(models.Model):
    new_plan = models.CharField(max_length=200)  # dodaj nowy plan
    new_step = models.CharField(max_length=200) # Dodaj nowy krok
    name_plan = models.CharField(max_length=200) # Nazwa planu
    name_step = models.CharField(max_length=200) # Nazwa kroku
    plan_remove = models.CharField(max_length=200) # Usuń plan (button)
    step_remove = models.CharField(max_length=200) # Usuń krok (button)
    remove_warning = models.CharField(max_length=200, blank=True, null=True) # Czy na pewno usunąć? (text)
    remove_permanent = models.CharField(max_length=200, blank=True, null=True) # Tak usuń trwale (button)
    dont_remove = models.CharField(max_length=200, blank=True, null=True) # Nie usuwaj (button)
    editme = models.CharField(max_length=200) # Edytuj
    switch_places = models.CharField(max_length=200) # Zamień miejscami (button)
    switch_with = models.CharField(max_length=200) # Zamień z krokiem:
    switch_text = models.CharField(max_length=200) # Zamień z innym krokiem w planie (text)
    u_edit_step_no = models.CharField(max_length=200) # Edytujesz krok nr.
    title = models.CharField(max_length=200) # Tytuł
    descr = models.CharField(max_length=200) # opis
    early_crop = models.CharField(max_length=200) # Wczesny Plon
    middle_crop = models.CharField(max_length=200, blank=True, null=True) # Śródplon
    late_crop = models.CharField(max_length=200) # late_crop
    destroy_early_crop = models.CharField(max_length=200) # Zniszcz wczesny plon na zielony nawóz
    destroy_middle_crop = models.CharField(max_length=200, blank=True, null=True) # Zniszcz śródplon na zielony nawóz
    destroy_late_crop = models.CharField(max_length=200) # Zniszcz późny plon na zielony nawóz
    add_fertilizer = models.CharField(max_length=200) # Dodaj nawóz
    add_fertilizer_onhover = models.CharField(max_length=800) # Wyjaśnienie co program rozumie przez nawóz w onhover nad ikonką "Info"
    change = models.CharField(max_length=200) # Zachowaj zmiany (button)
    publish = models.CharField(max_length=200, blank=True, null=True) # Opublikuj
    unpublish = models.CharField(max_length=200, blank=True, null=True) # Wycofaj
    publish_text = models.CharField(max_length=200, blank=True, null=True) # Opublikuj swój plan (text)
    unpublish_text = models.CharField(max_length=200, blank=True, null=True) # Wycofaj plan z publikacji (text)
    publish_onhover = models.CharField(max_length=900, blank=True, null=True) # Wyjaśnienie onhover o publikacji
    unpublish_onhover = models.CharField(max_length=900, blank=True, null=True) # Wyjaśnienie onhover o wycofywaniu publikacji
    more_info = models.CharField(max_length=900, blank=True, null=True) # więcej informacji (button "info")
    option_select = models.CharField(max_length=200, blank=True, null=True) # Wybierz opcję: (dropdown)
    in_this_plan = models.CharField(max_length=200, blank=True, null=True) # W tym planie znajduje się
    fabs_and = models.CharField(max_length=200, blank=True, null=True) # bobowatych lub strączkowych
    should_be_fabs = models.CharField(max_length=200, blank=True, null=True) # Powinno ich być między 25% a 33%
    error_len = models.CharField(max_length=200, blank=True, null=True) # Błąd: ten płodozmian jest za krótki.
    len_required = models.CharField(max_length=200, blank=True, null=True) # W płodozmianie znajdują się rośliny, które wymagają dłuższego zmianowania.
    remove_or_add = models.CharField(max_length=200, blank=True, null=True) # Usuń je i wybierz coś innego, lub dodaj więcej roślin.
    plan_limit_reached = models.TextField(blank=True, null=True) # Osiągnięto limit planów
    family = models.CharField(max_length=200, blank=True, null=True) # Rodzina
    species = models.CharField(max_length=200, blank=True, null=True) # Gatunki
    sources = models.CharField(max_length=200, blank=True, null=True) # Źródła
    notes = models.CharField(max_length=200, blank=True, null=True) # Uwagi
    allelopatic_conflict = models.CharField(max_length=200, blank=True, null=True) # Konflikt na tle allelopatycznym
    harms = models.CharField(max_length=200, blank=True, null=True) # Szkodzi
    in_step = models.CharField(max_length=200, blank=True, null=True) # W kroku
    well_cooperates = models.CharField(max_length=200, blank=True, null=True) # dobrze oddziaływuje na
    collides = models.CharField(max_length=200, blank=True, null=True) # Powoduje KOLIZJĘ z
    image_source = models.CharField(max_length=200, blank=True, null=True) # Źródło obrazka
    add_fertilizer_main = models.CharField(max_length=200, blank=True, null=True) # W tym planie brakuje nawozu z zewnątrz!
    add_fertilizer_onhover_main = models.CharField(max_length=300, blank=True, null=True) # Dowiedz się więcej o dodawaniu nawozów do płodozmianu.
    infl_type = models.CharField(max_length=100, blank=True, null=True) # typ oddziaływania
    companion = models.CharField(max_length=100, blank=True, null=True) # współrzędna
    following = models.CharField(max_length=100, blank=True, null=True) # następcza
    allelopatic = models.CharField(max_length=150, blank=True, null=True) # allelopatyczna, albo współrzędna i nastepcza
    source_button = models.CharField(max_length=50, blank=True, null=True) # Źródło
    known_interactions = models.CharField(max_length=200, blank=True, null=True) # Znane interakcje
    plant_to_other = models.CharField(max_length=200, blank=True, null=True) # Roślina oddziaływuje na inne
    other_to_plant = models.CharField(max_length=200, blank=True, null=True) # Inne oddziaływują na roślinę
    family_to_other = models.CharField(max_length=200, blank=True, null=True) # Rodzina oddziaływuje na inne
    other_to_family = models.CharField(max_length=200, blank=True, null=True) # Inne oddziaływują na rodzinę
    category_to_other = models.CharField(max_length=200, blank=True, null=True) # Kategoria oddziaływuje na inne
    other_to_category = models.CharField(max_length=200, blank=True, null=True) # Inne oddziaływują na kategorię
    annual = models.CharField(max_length=50, blank=True, null=True) # Jare
    perennial = models.CharField(max_length=50, blank=True, null=True) # Ozime
    evaluate_button = models.CharField(max_length=50, blank=True, null=True) # Ewaluacja (button)
    analysis_by_text = models.CharField(max_length=200, blank=True, null=True) # Analizuje plan pod kątem pozytywnych i negatywnych interakcji, oraz błędów.
    remove_element = models.CharField(max_length=50, blank=True, null=True) # Usuń element (button)
    add_element = models.CharField(max_length=50, blank=True, null=True) # Dodaj element (button)
    return_to_plan = models.CharField(max_length=50, blank=True, null=True) # Powrót do planu (button)
    categories = models.CharField(max_length=50, blank=True, null=True) # Kategorie
    next_year = models.CharField(max_length=50, blank=True, null=True) # W kolejnym roku
    second_year = models.CharField(max_length=50, blank=True, null=True) # W drugim roku
    third_year = models.CharField(max_length=50, blank=True, null=True) # W trzecim roku
    two_consecutive = models.CharField(max_length=50, blank=True, null=True) # W dwóch kolejnych latach

    class Meta:
        verbose_name_plural = 'Rotator Editor Page Names'


# klasa tłumaczeniowa dla strony "o nawozach"
class FertilizerPageNames(models.Model):
    title = models.CharField(max_length=50)
    descr = models.TextField()  # Intro o nawozach w ogóle
    elements_head = models.CharField(max_length=50,blank=True, null=True)  # Duży nagłówek "Składniki gleby", albo "Pierwiastki"
    makro_head = models.CharField(max_length=50,blank=True, null=True)  # Nagłówek makroelementy
    makro_descr = models.TextField(blank=True, null=True)  # Opis czym są makroelementy
    micro_head = models.CharField(max_length=50,blank=True, null=True)  # Nagłówek mikroelementy
    micro_descr = models.TextField(blank=True, null=True)  # Opis czym są mikroelementy
    fertilizers_head = models.CharField(max_length=50,blank=True, null=True)  # Duży nagłówek "Rodzaje nawozów"
    natural_fertilizers_head = models.CharField(max_length=50,blank=True, null=True)  # Nagłówek "nawozy naturalne"
    natural_fertilizers_descr = models.TextField(blank=True, null=True)  # Opis czym są nawozy naturalne.
    artificial_fertilizers_head = models.CharField(max_length=50,blank=True, null=True)  # Nagłówek nawozy sztuczne
    artificial_fertilizers_descr = models.TextField(blank=True, null=True)  # Opis czym są nawozy sztuczne.

    class Meta:
        verbose_name_plural = 'Fertilizer Page Names'


# klasa opisująca poszczególne pierwiastki chemiczne w glebie dla strony "o nawozach".
class BasicElement(models.Model):
    name = models.CharField(max_length=50)
    latin_name = models.CharField(max_length=50)
    symbol = models.CharField(max_length=2)
    image = models.ImageField(upload_to="images", blank=True, null=True)
    image_source = models.ForeignKey(
        "ElementDataString", on_delete=models.SET_NULL,
        related_name="set_image_eds_basic", blank=True, null=True
        )
    is_trace_element = models.BooleanField(default=True)
    descr = models.TextField()

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def summary(self):
        return self.descr[:150]


# klasa opisująca poszczególne nawozy - many-to-many do każdego zawartego w nim elementu?
class Fertilizer(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="images", blank=True, null=True)
    image_source = models.ForeignKey(
        "ElementDataString", on_delete=models.SET_NULL,
        related_name="set_image_eds_fertilizer", blank=True, null=True
        )
    descr = models.TextField()
    contains_elements = models.ManyToManyField(
        "BasicElement", related_name="contains_elements", blank=True)
    is_natural = models.BooleanField(default=False)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def summary(self):
        return self.descr[:150]


# Fizyczne źródła danych dot. nawozów np. z książek.
class FertilizerDataSource(models.Model):
    title = models.CharField(max_length=150)
    descr = models.TextField(blank=True, null=True)
    from_fertilizer = models.ForeignKey(
        "Fertilizer",
        related_name="fertilizer_source_set",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    at_data_string = models.ForeignKey(
        "ElementDataString",
        related_name="element_data_string_set",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    pages_from = models.IntegerField(blank=True, null=True)
    pages_to = models.IntegerField(blank=True, null=True)

    class Meta:
        ordering = ["from_fertilizer", "title"]

    def __str__(self):
        return self.title


# Część źródła danych w formia poszatkowanego stringa - reusable.
class ElementDataString(models.Model):
    title = models.CharField(max_length=150)
    part1 = models.CharField(max_length=500, blank=True, null=True)
    link = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title
