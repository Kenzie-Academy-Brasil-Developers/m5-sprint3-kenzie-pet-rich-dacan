from rest_framework import serializers

from .models import SexAnimals


class AnimalSerializer(serializers.Serializer):
    name = serializers.CharField()
    age = serializers.IntegerField()
    weight = serializers.FloatField()
    sex = serializers.ChoiceField(
        choices=SexAnimals.choices, default=SexAnimals.NOT_INFORMED
    )
