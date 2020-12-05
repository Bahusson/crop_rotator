from django.db import models
from django.contrib.auth.models import User  # Zaimportuj uproszczony model usera.


# Plan płodozmianu - potencjalnie przyporządkowany do użytkownika.
class RotationPlan(models.Model):
    CLASS_14A = 0
    CLASS_4B_LOW = 1
    SOIL_CLASS = (
    (CLASS_14A, "Gleby Dobrej Jakości"),
    (CLASS_4B_LOW, "Gleby Gorszej Jakości"),
    )
    title = models.CharField(max_length=150)
    owner = models.ForeignKey(
     User, on_delete=models.CASCADE, blank=True, null=True)
    pubdate = models.DateTimeField(blank=True, null=True)  # Data publikacji
    soil_type = models.PositiveSmallIntegerField(
                choices=SOIL_CLASS, default=0)

    class Meta:
        ordering = ['-pubdate']

    def __str__(self):
        return self.title

    def pubdate_short(self):
        return self.pubdate.strftime('%a %d %b %Y')


# Rodzina Botaniczna - zawiera informacje o typowych wartościach
# dla danej rodziny roślin
class CropFamily(models.Model):
    N_A = 0
    BETTERS = 1
    WORSENS = 2
    NEUTRAL = 3
    AGRICULTURE_STATUS = (
    (N_A, 'Nie Dotyczy'),
    (BETTERS, "Poprawia Jakość Gleby"),
    (WORSENS, "Pogarsza Jakość Gleby"),
    (NEUTRAL, "Neutralna Dla Jakości Gleby"),
    )
    name = models.CharField(max_length=150)
    latin_name = models.CharField(max_length=150, blank=True, null=True)
    culture = models.PositiveSmallIntegerField(
                choices=AGRICULTURE_STATUS, default=3)
    # W jakim stanie zostawia glebę po sobie.
    cooldown = models.IntegerField(blank=True, null=True)
    # Ile lat nie wolno uprawiać po sobie.
    is_manurable = models.BooleanField(default=False)
    # Czy wolno nawozić obornikiem i czy to poprawia kulturę gleby?
    culture_manured = models.PositiveSmallIntegerField(
                choices=AGRICULTURE_STATUS, default=0)
    # W jakiej kulturze zostawia po użyciu wraz z obornikiem?
    class Meta:
        ordering = ['-name']
        verbose_name_plural = 'Crop Families'

# Nie dla usera - model plonu/poplonu/międzyplonu
class Crop(models.Model):
    AS_FAMILY = 0
    BETTERS = 1
    WORSENS = 2
    NEUTRAL = 3
    AGRICULTURE_STATUS = (
    (AS_FAMILY, "Domyślnie dla Rodziny"),
    (BETTERS, "Poprawia Jakość Gleby"),
    (WORSENS, "Pogarsza Jakość Gleby"),
    (NEUTRAL, "Neutralna Dla Jakości Gleby"),
    )
    name = models.CharField(max_length=150)
    descr = models.CharField(max_length=500, blank=True, null=True)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    pubdate = models.DateTimeField(blank=True, null=True)  # Data publikacji
    family = models.ForeignKey(
     'CropFamily', on_delete=models.SET_NULL, blank=True, null=True)
    culture_override = models.PositiveSmallIntegerField(
                choices=AGRICULTURE_STATUS, default=0)
    cooldown_override = models.IntegerField(blank=True, null=True)
    is_summercrop = models.BooleanField(default=False)
    # Czy jest rośliną jarą niszczoną przez przymrozek?
    allelopatic_to = models.ManyToManyField('Crop', blank=True)
    # Wiemy, że nie pozwala po sobie uprawiać tych rzeczy,
    # ze względów allelopatycznych
    is_demanding = models.BooleanField(default=False)
    # Roślina wymagająca - tj. potrzebuje "lepszych" gleb pod uprawę.


    class Meta:
        ordering = ['-name']

    def __str__(self):
        return self.name


# Mieszanka na miedzyplon
class CropMix(models.Model):
    name = models.CharField(max_length=150)
    descr = models.CharField(max_length=500, blank=True, null=True)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    pubdate = models.DateTimeField(blank=True, null=True)  # Data publikacji
    ingredients = models.ManyToManyField('Crop', blank=True)

    class Meta:
        ordering = ['-name']
        verbose_name_plural = 'Crop Mixes'

    def __str__(self):
        return self.name


# Element płodozmianu.
class RotationStep(models.Model):
    title = models.CharField(max_length=150)
    descr = models.CharField(max_length=500, blank=True, null=True)
    add_manure = models.BooleanField(default=False)  # Czy dodać nawóz?
    from_plan = models.ForeignKey(
     'RotationPlan',related_name='rotation_plan_set', on_delete=models.CASCADE, blank=True, null=True)
    order = models.IntegerField(blank=True, null=True)
    # auto: kolejność w planie.
    crop = models.ForeignKey(
     'Crop',related_name='crop_main_set', on_delete=models.SET_NULL, blank=True, null=True)
    # Z listy: plon główny
    co_crop = models.ForeignKey(
     'Crop',related_name='co_crop_set', on_delete=models.SET_NULL, blank=True, null=True)
    # Z listy: Wsiewka / uprawa współrzędna
    after_crop = models.ForeignKey(
     'Crop',related_name='after_crop_set', on_delete=models.SET_NULL, blank=True, null=True)
    # Międzyplon typu "poplon"
    after_crop_mix = models.ForeignKey(
     'CropMix',related_name='crop_mix_set', on_delete=models.SET_NULL, blank=True, null=True)
    #
    is_ac_main = models.BooleanField(default=False)
    # Czy poplon jest rośliną ozimą z plonu głównego, którą zamierzamy zebrać
    # w przyszłym roku?
    # Jeśli tak, to powinien zajmować automatycznie
    # slot letni przyszłego roku.
    # (Domyślnie fałsz, pojawia się tylko jeśli is_summercrop = False)
    is_ac_harvest = models.BooleanField(default=False)
    # Czy zabieramy poplon z pola, czy go zostawiamy na zielony nawóz?
    # Pojawia się tylko wtedy jeśli roślina ma szanse przetrwać przymrozek



    class Meta:
        ordering = ['-from_plan', 'order']
        verbose_name_plural = 'Rotation Steps'

    def __str__(self):
        return self.title
