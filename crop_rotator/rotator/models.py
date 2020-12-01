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
        (OTHER, "każdy"),
        (FABACEAE, "Bobowate"),
        (FABACEAE_PERSISTENT, "Bobowate Wieloletnie"),
        )
    name = models.CharField(max_length=150)
    descr = models.CharField(max_length=500, blank=True, null=True)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    owner = models.ForeignKey(
     User, on_delete=models.CASCADE, blank=True, null=True)
    pubdate = models.DateTimeField(blank=True, null=True)  # Data publikacji
    bio_type = models.PositiveSmallIntegerField(
            choices=BOTANIC_FAMILY, default=3)

    class Meta:
        ordering = ['-name']

    def __str__(self):
        return self.title

    def pubdate_short(self):
        return self.pubdate.strftime('%a %d %b %Y')


# Mieszanka na miedzplon
class CropMix(models.Model):
    name = models.CharField(max_length=150)
    descr = models.CharField(max_length=500, blank=True, null=True)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    owner = models.ForeignKey(
     User, on_delete=models.CASCADE, blank=True, null=True)
    pubdate = models.DateTimeField(blank=True, null=True)  # Data publikacji
    # W tym miejscu trzeba machnąć jakąś listę,
    # która będzie się odnosić do już istniejących klas "Crop".


# Element płodozmianu.
class RotationStep(models.Model):
    title = models.CharField(max_length=150)
    descr = models.CharField(max_length=500, blank=True, null=True)
    from_plan = models.ForeignKey(
     'RotationPlan', on_delete=models.CASCADE, blank=True, null=True)
    order = models.IntegerField(blank=True, null=True)
    # auto: kolejność w planie.
    crop = models.ForeignKey(
     'Crop', on_delete=models.CASCADE, blank=True, null=True)
    # Z listy: plon główny
    co_crop = models.ForeignKey(
     'Crop', on_delete=models.CASCADE, blank=True, null=True)
    # Z listy: Wsiewka / uprawa współrzędna
    after_crop = models.ForeignKey(
     'Crop', on_delete=models.CASCADE, blank=True, null=True)
    # Międzyplon typu "poplon"
    after_crop_mix = models.ForeignKey(
     'CropMix', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        ordering = ['-from_plan', 'order']

    def __str__(self):
        return self.title
