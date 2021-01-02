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
    cooldown_min = models.IntegerField(blank=True, null=True)
    # Ile lat nie wolno uprawiać po sobie minimum.
    cooldown_max = models.IntegerField(blank=True, null=True)
    # Ile lat nie wolno uprawiać po sobie maximum.
    is_manurable = models.BooleanField(default=False)
    # Czy wolno nawozić obornikiem i czy to poprawia kulturę gleby?
    culture_manured = models.PositiveSmallIntegerField(
                choices=AGRICULTURE_STATUS, default=0)
    # W jakiej kulturze zostawia po użyciu wraz z obornikiem?
    is_mandatory_crop = models.BooleanField(default=False)
    # Czy musi występować w płodozmianie? (Bo trzeba wyróżnić Bobowate)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Crop Families'

    def __str__(self):
        return self.name


# Rodzaj plonu ze względów praktycznych np. "okopowe" - taki dodatkowy tag.
class CropTag(models.Model):
    name = models.CharField(max_length=150)
    descr = models.CharField(max_length=500, blank=True, null=True)
    image = models.ImageField(upload_to='images', blank=True, null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


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
    # Rozważ dodanie zajmowanego piętra w mieszance.
    N_A = 0
    LOWER = 1
    LOWER_MIDDLE = 2
    MIDDLE = 3
    MIDDLE_TOP = 4
    TOP = 5
    MIX_LEVEL = (
    (N_A, "Nieznane"),
    (LOWER, "Niższe"),
    (LOWER_MIDDLE, "Niższe-Średnie"),
    (MIDDLE, "Średnie"),
    (MIDDLE_TOP, "Średnie-Wyższe"),
    (TOP, "Wyższe"),
    )
    name = models.CharField(max_length=150)
    descr = models.CharField(max_length=500, blank=True, null=True)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    pubdate = models.DateTimeField(blank=True, null=True)  # Data publikacji
    family = models.ForeignKey(
     'CropFamily', on_delete=models.SET_NULL, blank=True, null=True)
    culture_override = models.PositiveSmallIntegerField(
                choices=AGRICULTURE_STATUS, default=0)
    cooldown_min_override = models.IntegerField(blank=True, null=True)
    cooldown_max_override = models.IntegerField(blank=True, null=True)
    is_summercrop = models.BooleanField(default=False)
    # Czy jest rośliną jarą niszczoną przez przymrozek?
    # Szczególnie istotne przy bobowatych dla triku wsiewka-main_crop.
    allelopatic_to = models.ManyToManyField(
        'Crop', related_name="known_antagonisms", blank=True)
    allelopatic_to_family = models.ManyToManyField(
        'CropFamily', related_name="known_antagonisms_family", blank=True)
    allelopatic_to_tag = models.ManyToManyField(
        'CropTag', related_name="known_antagonisms_tag", blank=True)
    # Wiemy, że nie pozwala po sobie i ze sobą uprawiać tych rzeczy,
    # ze względów allelopatycznych
    is_demanding = models.BooleanField(default=False)
    # Roślina wymagająca - tj. potrzebuje "lepszych" gleb pod uprawę.
    is_deep_roots = models.BooleanField(default=False)
    # Czy ma głęboki system korzeniowy?
    is_leaves_mess = models.BooleanField(default=False)
    # Czy zostawia dużo resztek pożniwnych?
    takes_mix_level = models.PositiveSmallIntegerField(
        choices=MIX_LEVEL, default=0)
    synergic_to = models.ManyToManyField(
        'Crop', related_name="known_synergies", blank=True)
    synergic_to_family = models.ManyToManyField(
        'CropFamily', related_name="known_synergies_family", blank=True)
    synergic_to_tag = models.ManyToManyField(
        'CropTag', related_name="known_synergies_tag", blank=True)
    # Znane synergie w uprawie współrzędnej. Jako przedplon będzie inna klasa.
    tags = models.ManyToManyField(
        'CropTag', related_name="special_tags", blank=True)
    # dodatkowe cechy plonu wyrażone w tagach.
    seed_norm_min = models.IntegerField(blank=True, null=True)
    # minimalna norma wysiewu w kg/ha
    seed_norm_max = models.IntegerField(blank=True, null=True)
    # maksymalna norma wysiewu w kg/ha

    class Meta:
        ordering = ['family', 'name']

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
        ordering = ['name']
        verbose_name_plural = 'Crop Mixes'

    def __str__(self):
        return self.name


# Element płodozmianu.
class RotationStep(models.Model):
    title = models.CharField(max_length=150)
    descr = models.CharField(max_length=500, blank=True, null=True)
    add_manure = models.BooleanField(default=False)  # Czy dodać nawóz?
    from_plan = models.ForeignKey(
     'RotationPlan', related_name='rotation_plan_set',
     on_delete=models.CASCADE, blank=True, null=True)
    order = models.IntegerField(blank=True, null=True)
    # auto: kolejność w planie.
    early_crop = models.ManyToManyField(
     'Crop', related_name='crop_early_set', blank=True)
    # Z listy: plon główny
    late_crop = models.ManyToManyField(
     'Crop', related_name='crop_late_set', blank=True)
    # Międzyplon typu "poplon"
    is_late_crop_destroy = models.BooleanField(default=False)
    # Czy plon późny zostanie zniszczony na zielony nawóz?
    # Jeśli nie to przyjmujemy, że zostaje zebrany np. na siano lub na ziarno.
    # Istotne dla monitorowania przez program kultury gleby
    is_early_crop_destroy = models.BooleanField(default=False)
    # Czy plon wczesny zostanie zniszczony na zielony nawóz?
    # Jeśli nie to przyjmujemy, że zostaje zebrany np. na siano lub na ziarno.
    # Istotne dla monitorowania przez program kultury gleby

    class Meta:
        ordering = ['-from_plan', 'order']
        verbose_name_plural = 'Rotation Steps'

    def __str__(self):
        return self.title


# Fizyczne źródła danych np. z książek.
class CropDataSource(models.Model):
    title = models.CharField(max_length=150)
    descr = models.CharField(max_length=500, blank=True, null=True)
    from_plan = models.ForeignKey(
     'Crop', related_name='crop_source_set',
     on_delete=models.CASCADE, blank=True, null=True)
    at_tag = models.ManyToManyField(
     'CropTag', related_name='crop_source_tag_set', blank=True)
    at_data_string = models.ForeignKey(
     'CropDataString', related_name='crop_data_string_set',
     on_delete=models.SET_NULL, blank=True, null=True)
    pages_from = models.IntegerField(blank=True, null=True)
    pages_to = models.IntegerField(blank=True, null=True)


# Część źródła danych w formia poszatkowanego stringa - reusable.
class CropDataString(models.Model):
    title = models.CharField(max_length=150)
    part1 = models.CharField(max_length=500, blank=True, null=True)
    part2 = models.CharField(max_length=500, blank=True, null=True)

# Tutaj jeszcze trzeba zrobić klasy tłumaczeniowe dla kultury gleby, oraz poziomu w mieszance
