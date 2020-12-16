from django.db import models


# Klasa tłumaczeniowa dla "core"
class PageNames(models.Model):
    lang_flag = models.ImageField(upload_to='images')  # Mały obrazek języka
    headtitle = models.CharField(max_length=200)  # Nagłówek strony w tym j
    mainpage = models.CharField(max_length=200)  # Strona główna w tym języku
    about = models.CharField(max_length=200)  # Informacje w tym języku
    contact = models.CharField(max_length=200)  # Kontakty w tym języku
    logout = models.CharField(max_length=200)  # Wyloguj
    login = models.CharField(max_length=200)  # zaloguj
    register = models.CharField(max_length=50)
    see_more = models.CharField(max_length=200)
    editme = models.CharField(max_length=200)  # edytuj

    class Meta:
        verbose_name_plural = 'Page Names'


# Klasa tłumaczeniowa dla Login/Register i myprofile.
class RegNames(models.Model):
    password = models.CharField(max_length=50, null=True)
    re_password = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=50, null=True)

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
class AboutPageNames (models.Model):
    about_project = models.TextField()  # Pole tekstowe dla strony about.
    send_email = models.CharField(max_length=200)  # Wyślij email
    gitter = models.CharField(max_length=200)  # Adres gittera
    github = models.CharField(max_length=200)  # Adres github
    login_to_see = models.CharField(max_length=200)  # zaloguj się by przeglądać

    class Meta:
        verbose_name_plural = 'Registry Names'
