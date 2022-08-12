from django.db import models


class SexAnimals(models.TextChoices):
    MACHO = "Macho"
    FÊMEA = "Fêmea"
    NOT_INFORMED = "Não Informado"


class Animal(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    weight = models.FloatField()
    sex = models.CharField(
        max_length=15, choices=SexAnimals.choices, default=SexAnimals.NOT_INFORMED
    )

    group = models.OneToOneField(
        "groups.Group", on_delete=models.CASCADE, related_name="animals"
    )

    traits = models.ManyToManyField("traits.Trait", related_name="animals")