from django.db import models
from django.contrib.auth.models import User


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
     User, related_name="rotation_plan_owner_set0",
     on_delete=models.CASCADE, blank=True, null=True)
    pubdate = models.DateTimeField(blank=True, null=True)  # Data publikacji
    soil_type = models.PositiveSmallIntegerField(choices=SOIL_CLASS, default=0)
    published = models.BooleanField(default=False)  # Czy ma być widoczny na głównej.

    class Meta:
        ordering = ["-pubdate"]

    def __str__(self):
        return self.title

    def pubdate_short(self):
        return self.pubdate.strftime("%a %d %b %Y")


# Element płodozmianu.
class RotationStep(models.Model):
    title = models.CharField(max_length=150)
    descr = models.CharField(max_length=500, blank=True, null=True)
    add_manure_early = models.BooleanField(default=False)
    add_manure_middle = models.BooleanField(default=False)
    add_manure_late = models.BooleanField(default=False)
    from_plan = models.ForeignKey(
        "RotationPlan",
        related_name="rotation_plan_set0",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    order = models.IntegerField(blank=True, null=True)
    # auto: kolejność w planie.
    early_crop = models.ManyToManyField(
        "rotator.Crop", related_name="crop_early_set0", blank=True
    )
    middle_crop = models.ManyToManyField(
        "rotator.Crop", related_name="crop_middle_set0", blank=True
    )
    # Z listy: plon główny
    late_crop = models.ManyToManyField(
     "rotator.Crop", related_name="crop_late_set0", blank=True)
    # Międzyplon typu "poplon"
    is_late_crop_destroy = models.BooleanField(default=False)
    # Czy plon późny zostanie zniszczony na zielony nawóz?
    # Jeśli nie to przyjmujemy, że zostaje zebrany np. na siano lub na ziarno.
    # Istotne dla monitorowania przez program kultury gleby
    is_middle_crop_destroy = models.BooleanField(default=False)
    # Czy śróplon zostanie zniszczony na zielony nawóz?
    # Jeśli nie to przyjmujemy, że zostaje zebrany np. na siano lub na ziarno.
    # Istotne dla monitorowania przez program kultury gleby
    is_early_crop_destroy = models.BooleanField(default=False)
    # Czy plon wczesny zostanie zniszczony na zielony nawóz?
    # Jeśli nie to przyjmujemy, że zostaje zebrany np. na siano lub na ziarno.
    # Istotne dla monitorowania przez program kultury gleby

    class Meta:
        ordering = ["-from_plan", "order"]
        verbose_name_plural = "Rotation Steps"

    def __str__(self):
        return self.title
