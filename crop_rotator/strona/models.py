from django.db import models


# Klasa tłumaczeniowa dla "core"
class PageNames(models.Model):
    lang_flag = models.ImageField(upload_to='images')  # Mały obrazek języka
    headtitle = models.CharField(max_length=200)  # Nagłówek strony w tym j
    mainpage = models.CharField(max_length=200)  # Strona główna w tym języku
    all_plants = models.CharField(max_length=200, blank=True, null=True) # Spis roślin
    about = models.CharField(max_length=200)  # Informacje w tym języku
    contact = models.CharField(max_length=200)  # Kontakty w tym języku
    logout = models.CharField(max_length=200)  # Wyloguj
    login = models.CharField(max_length=200)  # zaloguj
    register = models.CharField(max_length=50)
    see_more = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Page Names'


# Klasa tłumaczeniowa dla Login/Register i myprofile.
class RegNames(models.Model):
    password = models.CharField(max_length=50, blank=True, null=True)
    re_password = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    refresh = models.CharField(max_length=50, blank=True, null=True)

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
    editme = models.CharField(max_length=200) # Edytuj
    switch_places = models.CharField(max_length=200) # Zamień miejscami (button)
    switch_with = models.CharField(max_length=200) # Zamień z krokiem:
    switch_text = models.CharField(max_length=200) # Zamień z innym krokiem w planie (text)
    u_edit_step_no = models.CharField(max_length=200) # Edytujesz krok nr.
    title = models.CharField(max_length=200) # Tytuł
    descr = models.CharField(max_length=200) # opis
    early_crop = models.CharField(max_length=200) # Wczesny Plon
    late_crop = models.CharField(max_length=200) # late_crop
    destroy_early_crop = models.CharField(max_length=200) # Zniszcz wczesny plon na zielony nawóz
    destroy_late_crop = models.CharField(max_length=200) # Zniszcz późny plon na zielony nawóz
    add_fertilizer = models.CharField(max_length=200) # Dodaj nawóz
    add_fertilizer_onhover = models.CharField(max_length=800) # Wyjaśnienie co program rozumie przez nawóz w onhover nad ikonką "Info"
    change = models.CharField(max_length=200) # Zachowaj zmiany (button)

    class Meta:
        verbose_name_plural = 'Rotator Editor Page Names'
