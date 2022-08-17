import math

from groups.models import Group
from groups.serializers import GroupSerializer
from rest_framework import serializers, status
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
    age_in_human_years = serializers.SerializerMethodField()

    def create(self, validated_data: dict):
        group_info = validated_data.pop("group")
        traits = validated_data.pop("traits")

        group, _ = Group.objects.get_or_create(**group_info)

        animal_obj = Animal.objects.create(**validated_data, group=group)

        for trait in traits:
            trait, _ = Trait.objects.get_or_create(**trait)
            animal_obj.traits.add(trait)

        return animal_obj

    def update(self, instance, validated_data: dict):
        non_updatable = {"sex", "group", "traits"}

        for key, value in validated_data.items():
            if key in non_updatable:
                raise KeyError(
                    {f"{key}": f"You can not update {key} property."},
                    status.HTTP_422_UNPROCESSABLE_ENTITY,
                )

            # elif key == "traits":
            #     for traits in value:
            #         trait, _ = traits.objects.get_or_create(**trait)
            #         instance.traits.add(trait)
            else:
                setattr(instance, key, value)

        instance.save()

        return instance

    def get_age_in_human_years(self, obj: Animal) -> float:

        human_age = round(16 * math.log(obj.age) + 31)

        return human_age


#  def update(self, instance, validated_data: dict):
#         non_updatable = {"sex", "group", "traits"}

#         try:
#             for key, value in validated_data.items():
#                 if key in non_updatable:

#                     setattr(instance, key, value)

#         except Http404:
#             return {
#                 f"{key}": f"You can not update {key} property."
#             }, status.HTTP_422_UNPROCESSABLE_ENTITY

#         instance.save()

#         return instance
