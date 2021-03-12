from django.db import models

# Klasa uproszczonego panelu admina aplikacji.
class RotatorAdminPanel(models.Model):
    # Maksymalna ilość kroków w planie.
    max_steps = models.IntegerField()
    # Maksymalna ilość planów na użytkownika.
    max_user_plans = models.IntegerField()
    # Ile "lurk_plan" ma się cachować w minutach.
    # Oszczędza zasoby.
    lurk_plan_cooldown = models.IntegerField()
    # Ile strona ewaluacji ma się cachować w sekundach.
    # Przeciwdziała bezmyślnemu klikaniu.
    evaluated_plan_cooldown = models.IntegerField()
