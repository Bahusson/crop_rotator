from django.db import models
from django.contrib.auth.models import User  # Zaimportuj uproszczony model usera.


# Rodzina Botaniczna - zawiera informacje o typowych wartościach
# dla danej rodziny roślin
class CropFamily(models.Model):
    N_A = 0
    BETTERS = 1
    WORSENS = 2
    NEUTRAL = 3
    AGRICULTURE_STATUS = (
        (N_A, "Nie Dotyczy"),
        (BETTERS, "Poprawia Jakość Gleby"),
        (WORSENS, "Pogarsza Jakość Gleby"),
        (NEUTRAL, "Neutralna Dla Jakości Gleby"),
    )
    name = models.CharField(max_length=150)
    latin_name = models.CharField(max_length=150, blank=True, null=True)
    culture = models.PositiveSmallIntegerField(choices=AGRICULTURE_STATUS, default=3)
    # W jakim stanie zostawia glebę po sobie.
    cooldown_min = models.IntegerField(blank=True, null=True)
    # Ile lat nie wolno uprawiać po sobie minimum.
    cooldown_max = models.IntegerField(blank=True, null=True)
    # Ile lat nie wolno uprawiać po sobie maximum.
    is_manurable = models.BooleanField(default=False)
    # Czy wolno nawozić obornikiem i czy to poprawia kulturę gleby?
    culture_manured = models.PositiveSmallIntegerField(
        choices=AGRICULTURE_STATUS, default=0
    )
    # W jakiej kulturze zostawia po użyciu wraz z obornikiem?
    is_mandatory_crop = models.BooleanField(default=False)
    # Czy musi występować w płodozmianie? (Bo trzeba wyróżnić Bobowate)
    family_relationships = models.ManyToManyField(
        "FamilyInteraction", related_name="known_family_interactions", blank=True
    )
    is_family_slave = models.BooleanField(default=False)
    # Czy jest programistycznym podtypem rodziny
    # (np. workaround dla Owsa jako rodziny fitosanitarnej)
    family_master = models.ForeignKey(
        "CropFamily",
        related_name="family_subtype_set",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    family_slaves = models.ManyToManyField(
        "CropFamily", related_name="family_slaves_set", blank=True
    )

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Crop Families"

    def __str__(self):
        return self.name

    def get_cname(self):
        class_name = "CropFamily"
        return class_name


# Rodzaj plonu ze względów praktycznych np. "okopowe" - taki dodatkowy tag.
class CropTag(models.Model):
    name = models.CharField(max_length=150)
    descr = models.CharField(max_length=500, blank=True, null=True)
    image = models.ImageField(upload_to="images", blank=True, null=True)
    crop_relationships = models.ManyToManyField(
        "TagsInteraction", related_name="known_tags_interactions", blank=True
    )
    is_featured = models.BooleanField(default=False)  # Czy widoczny na głównej?

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_cname(self):
        class_name = "CropTag"
        return class_name


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
    ANNUAL = 0
    BIENNIAL = 1
    PERENNIAL = 2
    PLANT_TYPE = (
        (ANNUAL, "Roczna"),
        (BIENNIAL, "Dwuletnia"),
        (PERENNIAL, "Wieloletnia"),
    )
    name = models.CharField(max_length=150)
    latin_name = models.CharField(max_length=150, blank=True, null=True)
    descr = models.CharField(max_length=500, blank=True, null=True)
    image = models.ImageField(upload_to="images", blank=True, null=True)
    image_source = models.ForeignKey(
        "CropImageString", on_delete=models.SET_NULL,
        related_name="set_image_cds", blank=True, null=True
        )
    pubdate = models.DateTimeField(blank=True, null=True)  # Data publikacji
    family = models.ForeignKey(
        "CropFamily", on_delete=models.SET_NULL, related_name="set_family",
         blank=True, null=True
    )
    culture_override = models.PositiveSmallIntegerField(
        choices=AGRICULTURE_STATUS, default=0
    )
    cooldown_min_override = models.IntegerField(blank=True, null=True)
    cooldown_max_override = models.IntegerField(blank=True, null=True)
    crop_relationships = models.ManyToManyField(
        "CropsInteraction", related_name="known_crops_interactions", blank=True
    )
    is_demanding = models.BooleanField(default=False)
    # Roślina wymagająca - tj. potrzebuje "lepszych" gleb pod uprawę.
    is_deep_roots = models.BooleanField(default=False)
    # Czy ma głęboki system korzeniowy?
    is_leaves_mess = models.BooleanField(default=False)
    # Czy zostawia dużo resztek pożniwnych?
    takes_mix_level = models.PositiveSmallIntegerField(choices=MIX_LEVEL, default=0)
    tags = models.ManyToManyField("CropTag", related_name="special_tags", blank=True)
    # dodatkowe cechy plonu wyrażone w tagach.
    seed_norm_min = models.IntegerField(blank=True, null=True)
    # minimalna norma wysiewu w kg/ha
    seed_norm_max = models.IntegerField(blank=True, null=True)
    # maksymalna norma wysiewu w kg/ha
    plant_type = models.PositiveSmallIntegerField(choices=PLANT_TYPE, default=0)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_cname(self):
        class_name = "Crop"
        return class_name

# TODO: Wsiewki i miksy. Gotowe klasy do odhaszowania jak znajdzie się czas. :)
# Klasa dla wsiewek. Jeśli zachowują się wtedy inaczej niż normalnie.
#class InCrop(Crop):
#    is_slave_to = models.ForeignKey(
#        "Crop", on_delete=models.CASCADE, related_name="set_master_crop_in",
#        blank=True, null=True
#        )

# Klasa dla miksów. Jesli zachowują się wtedy inaczej niż normalnie.
#class MixedCrop(Crop):
#    is_slave_to = models.ForeignKey(
#        "Crop", on_delete=models.CASCADE, related_name="set_master_crop_mix",
#        blank=True, null=True
#        )

# Mieszanka na miedzyplon
class CropMix(models.Model):
    name = models.CharField(max_length=150)
    descr = models.CharField(max_length=500, blank=True, null=True)
    image = models.ImageField(upload_to="images", blank=True, null=True)
    pubdate = models.DateTimeField(blank=True, null=True)  # Data publikacji
    ingredients = models.ManyToManyField("Crop", blank=True)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Crop Mixes"

    def __str__(self):
        return self.name


# Podstawowa klasa interakcji - niewidoczna w adminie -
# od której dla wygody wyciągam pomniejsze poniżej.
class CropInteraction(models.Model):
    CO_CROP = 0
    ALLELOPATIC = 1
    NEXT_CROP = 2
    INTERACTION_TYPE = (
        (CO_CROP, "Współrzędne"),
        (ALLELOPATIC, "Allelopatyczne"),
        (NEXT_CROP, "Następcze"),
    )
    N_A = 0
    ANNUAL = 1
    PERENNIAL = 2
    CROP_TYPE = (
        (N_A, "Nie Dotyczy"),
        (ANNUAL, "Jare"),
        (PERENNIAL, "Ozime"),
    )
    title = models.CharField(max_length=150)  # Tytuł i od razu opis relacji
    is_positive = models.BooleanField(default=True)  # Typ oddziaływania
    about_crop = models.ForeignKey(
        "Crop",
        related_name="crop_interaction_set",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    about_family = models.ForeignKey(
        "CropFamily",
        related_name="family_interaction_set",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    about_tag = models.ForeignKey(
        "CropTag",
        related_name="tag_interaction_set",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    info_source = models.ForeignKey(
        "CropDataSource",
        related_name="info_source_set",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    type_of_interaction = models.PositiveSmallIntegerField(
        choices=INTERACTION_TYPE, default=0
    )
    season_of_interaction = models.PositiveSmallIntegerField(
        choices=CROP_TYPE, default=0
    )

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title

class CropsInteraction(CropInteraction):
    class Meta:
        ordering = ["title"]

    def __str__(self):
            return self.title


class FamilyInteraction(CropInteraction):
    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title


class TagsInteraction(CropInteraction):
    class Meta:
        ordering = ["title"]

    def __str__(self):
            return self.title


# Fizyczne źródła danych dot. roślin np. z książek.
class CropDataSource(models.Model):
    title = models.CharField(max_length=150)
    descr = models.TextField(blank=True, null=True)
    from_crop = models.ForeignKey(
        "Crop",
        related_name="crop_source_set",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    at_tag = models.ManyToManyField(
        "CropTag", related_name="crop_source_tag_set", blank=True
    )
    at_data_string = models.ForeignKey(
        "CropBookString",
        related_name="crop_data_string_set",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    pages_from = models.IntegerField(blank=True, null=True)
    pages_to = models.IntegerField(blank=True, null=True)
    order = models.IntegerField(blank=True, null=True)

    class Meta:
        ordering = ["-from_crop", "order", "title"]

    def __str__(self):
        return self.title


# Fizyczne źródła danych dot. rodzin np. z książek.
class CropDataFamilySource(CropDataSource):
    from_family = models.ForeignKey(
        "CropFamily",
        related_name="crop_data_family_source_set",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )


# Fizyczne źródła danych dot. rodzin np. z książek.
class CropDataTagSource(CropDataSource):
    from_tag = models.ForeignKey(
        "CropTag",
        related_name="crop_data_tag_source_set",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

# Część źródła danych w formia poszatkowanego stringa - reusable.
class CropDataString(models.Model):
    title = models.CharField(max_length=150)
    part1 = models.CharField(max_length=500, blank=True, null=True)
    link = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title


class CropBookString(CropDataString):

        class Meta:
            ordering = ["part1"]

        def __str__(self):
            return self.title

class CropImageString(CropDataString):

        class Meta:
            ordering = ["title"]

        def __str__(self):
            return self.title

# Tutaj jeszcze trzeba zrobić klasy tłumaczeniowe dla kultury gleby, oraz poziomu w mieszance
