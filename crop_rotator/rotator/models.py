from django.db import models


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
        choices=AGRICULTURE_STATUS, default=0
    )
    # W jakiej kulturze zostawia po użyciu wraz z obornikiem?
    is_mandatory_crop = models.BooleanField(default=False)
    # Czy musi występować w płodozmianie? (Bo trzeba wyróżnić Bobowate)
    crop_relationships = models.ManyToManyField(
        "FamilyInteraction", related_name="known_family_interactions",
        blank=True,
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
    takes_mix_level = models.PositiveSmallIntegerField(
        choices=MIX_LEVEL, default=0)
    tags = models.ManyToManyField(
        "CropTag", related_name="special_tags", blank=True)
    # dodatkowe cechy plonu wyrażone w tagach.
    seed_norm_min = models.IntegerField(blank=True, null=True)
    # minimalna norma wysiewu w kg/ha
    seed_norm_max = models.IntegerField(blank=True, null=True)
    # maksymalna norma wysiewu w kg/ha
    plant_type = models.PositiveSmallIntegerField(choices=PLANT_TYPE, default=0)
    meta_tags_source = models.TextField(blank=True, null=True)
    is_crop_mix = models.BooleanField(default=False)
    is_fertilizer = models.BooleanField(default=False)
    redirect_name = models.CharField(max_length=10, blank=True, null=True)
    redirect_id = models.IntegerField(blank=True, null=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_cname(self):
        class_name = "Crop"
        return class_name


class MixCrop(Crop):
    meta_tags = models.TextField(blank=True, null=True)



# Nieużywany na razie mix do mieszanek typu "Biomax".
# Mechanika na glo boardzie.
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
    SECOND_YEAR = 3
    THIRD_YEAR = 4
    TWO_CONSECUTIVE = 5
    NEXT_YEAR = 6
    INTERACTION_TYPE = (
        (CO_CROP, "Współrzędne"),
        (ALLELOPATIC, "Allelopatyczne"),
        (NEXT_CROP, "Następcze"),
        (SECOND_YEAR, "W drugim roku"),
        (THIRD_YEAR, "W trzecim roku"),
        (TWO_CONSECUTIVE, "W dwóch kolejnych latach"),
        (NEXT_YEAR, "W kolejnym roku"),
    )
    N_A = 0
    ANNUAL = 1
    PERENNIAL = 2
    CROP_TYPE = (
        (N_A, "Nie Dotyczy"),
        (ANNUAL, "Jare"),
        (PERENNIAL, "Ozime"),
    )
    NONE = 0
    FALSE = 1
    TRUE = 2
    SIGNS = (
        (NONE, "Brak"),
        (FALSE, "Szkodzi"),
        (TRUE, "Wspiera"),
    )
    title = models.CharField(max_length=150)  # Tytuł i od razu opis relacji
    signature = models.CharField(max_length=150, blank=True, null=True)  # Sygnatura dla serwera.
    # Poniżej do wywalenia po konwersji
    is_positive = models.BooleanField(default=True)  # Typ oddziaływania
    interaction_sign = models.PositiveSmallIntegerField(
     choices=SIGNS, default=0
    )
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
    is_server_generated = models.BooleanField(default=False)
    server_interaction = models.ForeignKey(
        "CropInteraction",
        related_name="server_interaction_set",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    debug_line = models.CharField(max_length=20, blank=True, null=True)
    trigger_crop = models.ForeignKey(
        "Crop",
        related_name="trigger_crop_set",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    trigger_tag = models.ForeignKey(
        "CropTag",
        related_name="tag_tag_set",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    @classmethod
    def create(cls, *args):
        interaction = cls(
         title=args[0],
         is_positive=args[1],
         about_crop=args[2],
         about_family=args[3],
         about_tag=args[4],
         info_source=args[5],
         type_of_interaction=args[6],
         season_of_interaction=args[7],
         is_server_generated=args[8],
         server_interaction=args[9],
         debug_line=args[10],
         trigger_crop=args[11],
         trigger_tag=args[12],
         )
        return interaction

    class Meta:
        ordering = ["is_server_generated" ,"title"]

    def __str__(self):
        return self.title


class CropsInteraction(CropInteraction):
    class Meta:
        ordering = ["is_server_generated" ,"title"]

    def __str__(self):
        return self.title


class FamilyInteraction(CropInteraction):
    class Meta:
        ordering = ["is_server_generated" ,"title"]

    def __str__(self):
        return self.title


class TagsInteraction(CropInteraction):
    class Meta:
        ordering = ["is_server_generated" ,"title"]

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
