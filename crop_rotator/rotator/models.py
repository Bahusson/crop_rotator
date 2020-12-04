from django.db import models
from django import User  # Zaimportuj uproszczony model usera.


# Plan płodozmianu - potencjalnie przyporządkowany do użytkownika.
class RotationPlan(models.Model):
    title = models.CharField(max_length=150)
    owner = models.ForeignKey(
     User, on_delete=models.CASCADE, blank=True, null=True)
    pubdate = models.DateTimeField(blank=True, null=True)  # Data publikacji

    class Meta:
        ordering = ['-pubdate']

    def __str__(self):
        return self.title

    def pubdate_short(self):
        return self.pubdate.strftime('%a %d %b %Y')


# Nie dla usera - model plonu/poplonu/międzyplonu
class Crop(models.Model):
    BRASSICACEAE = 0
    POACEAE = 1
    POACEAE_SEASONAL = 2
    OTHER = 3
    FABACEAE = 4
    FABACEAE_PERSISTENT = 5
    BOTANIC_FAMILY = (
        (BRASSICACEAE, "Kapustowate"),
        (POACEAE, "Wiechlinowate"),
        (POACEAE_SEASONAL, "Wiechlinowate Jednoroczne"),
        (OTHER, "Inne"),
        (FABACEAE, "Bobowate"),
        (FABACEAE_PERSISTENT, "Bobowate Wieloletnie"),
        )
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
    owner = models.ForeignKey(
     User, on_delete=models.SET_NULL, blank=True, null=True)
    pubdate = models.DateTimeField(blank=True, null=True)  # Data publikacji
    bio_type = models.PositiveSmallIntegerField(
            choices=BOTANIC_FAMILY, default=3)
    culture_override = models.PositiveSmallIntegerField(
                choices=AGRICULTURE_STATUS, default=0)
    #
    #
    #
    #
    # Poniższe jest opcjonalne imho. Dodać w rozszerzeniu jak będzie czas.
    is_summercrop = models.BooleanField(default=False)
    # Czy jest rośliną jarą niszczoną przez przymrozek?

    class Meta:
        ordering = ['-name']

    def __str__(self):
        return self.title


# Mieszanka na miedzyplon
class CropMix(models.Model):
    name = models.CharField(max_length=150)
    descr = models.CharField(max_length=500, blank=True, null=True)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    owner = models.ForeignKey(
     User, on_delete=models.SET_NULL, blank=True, null=True)
    pubdate = models.DateTimeField(blank=True, null=True)  # Data publikacji
    ingredients = models.ManyToManyField('Crop', blank=True, null=True)

    class Meta:
        ordering = ['-name']

    def __str__(self):
        return self.title


# Element płodozmianu.
class RotationStep(models.Model):
    title = models.CharField(max_length=150)
    descr = models.CharField(max_length=500, blank=True, null=True)
    add_manure = models.BooleanField(default=False)  # Czy dodać nawóz?
    from_plan = models.ForeignKey(
     'RotationPlan', on_delete=models.CASCADE, blank=True, null=True)
    order = models.IntegerField(blank=True, null=True)
    # auto: kolejność w planie.
    crop = models.ForeignKey(
     'Crop', on_delete=models.SET_NULL, blank=True, null=True)
    # Z listy: plon główny
    co_crop = models.ForeignKey(
     'Crop', on_delete=models.SET_NULL, blank=True, null=True)
    # Z listy: Wsiewka / uprawa współrzędna
    after_crop = models.ForeignKey(
     'Crop', on_delete=models.SET_NULL, blank=True, null=True)
    # Międzyplon typu "poplon"
    after_crop_mix = models.ForeignKey(
     'CropMix', on_delete=models.SET_NULL, blank=True, null=True)
    #
    #
    #
    #
    # Poniższe jest opcjonalne imho. Dodać w rozszerzeniu jak będzie czas.
    is_ac_main = models.BooleanField(default=False)
    # Czy poplon jest rośliną ozimą z plonu głównego, którą zamierzamy zebrać
    # w przyszłym roku?
    #(Domyślnie fałsz, pojawia się tylko jeśli is_summercrop = False)
    is_ac_harvest = models.BooleanField(default=False)
    # Czy zabieramy poplon z pola, czy go zostawiamy na zielony nawóz?
    # Pojawia się tylko wtedy jeśli roślina ma szanse przetrwać przymrozek



    class Meta:
        ordering = ['-from_plan', 'order']

    def __str__(self):
        return self.title
