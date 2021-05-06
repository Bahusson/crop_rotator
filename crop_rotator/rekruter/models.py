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
    pubdate = models.DateTimeField(blank=True, null=True)
    soil_type = models.PositiveSmallIntegerField(choices=SOIL_CLASS, default=0)
    published = models.BooleanField(default=False)

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
    from_plan = models.ForeignKey(
        "RotationPlan",
        related_name="rotation_plan_set0",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    order = models.IntegerField(blank=True, null=True)
    # auto: kolejność w planie.

    class Meta:
        ordering = ["-from_plan", "order"]
        verbose_name_plural = "Rotation Steps"

    def __str__(self):
        return self.title


# Podkrok elementu płodozmianu.
class RotationSubStep(models.Model):
    EARLY = 1
    MIDDLE = 2
    LATE = 3
    LOCAL_ORDER = (
        (EARLY, "Plon Wczesny"),
        (MIDDLE, "Śródplon"),
        (LATE, "Plon Późny"),
    )
    order = models.PositiveSmallIntegerField(choices=LOCAL_ORDER, default=0)
    from_step = models.ForeignKey(
            "RotationStep",
            related_name="rotation_step_set",
            on_delete=models.CASCADE,
            blank=True,
            null=True,
        )
    crop_substep = models.ManyToManyField(
        "rotator.Crop", related_name="crop_subtep_set", blank=True
    )
    add_manure = models.BooleanField(default=False)
    is_crop_destroy = models.BooleanField(default=False)

    @classmethod
    def create(cls, *args):
        substep = cls(
         order=args[0],
         from_step=args[1],
         )
        return substep

    class Meta:
        ordering = ["-from_step", "order"]
        verbose_name_plural = "Rotation Substeps"

    def __str__(self):
        return self.from_step.title + " (" + str(self.order) +")"
