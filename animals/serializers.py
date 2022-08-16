from groups.models import Group
from groups.serializers import GroupSerializer
from rest_framework import serializers
from traits.models import Trait
from traits.serializers import TraitSerializer

from .models import Animal, SexAnimals


class AnimalSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    age = serializers.IntegerField()
    weight = serializers.FloatField()
    sex = serializers.ChoiceField(
        choices=SexAnimals.choices, default=SexAnimals.NOT_INFORMED
    )
    group = GroupSerializer()
    traits = TraitSerializer(many=True)

    def create(self, validated_data: dict):
        group_info = validated_data.pop("group")
        traits = validated_data.pop("traits")

        group, _ = Group.objects.get_or_create(**group_info)

        animal_obj = Animal.objects.create(**validated_data, group=group)

        for trait in traits:
            trait, _ = Trait.objects.get_or_create(**trait)
            animal_obj.traits.add(trait)

        return animal_obj
