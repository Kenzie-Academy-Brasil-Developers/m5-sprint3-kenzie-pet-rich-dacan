from animals.models import Animal
from django.core.exceptions import ValidationError
from django.test import TestCase
from groups.models import Group


class GroupTestCase(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.group_data = {"name": "cão", "scientific_name": "canis familiaris"}

        cls.group_data_without_name = {"scientific_name": "canis familiaris"}

        cls.group_data_without_specific_name = {"name": "cão"}

        cls.group = Group.objects.create(**cls.group_data)

    def test_group_fields(self) -> None:

        self.assertEqual(self.group.name, self.group_data["name"])
        self.assertEqual(self.group.scientific_name, self.group_data["scientific_name"])

        print("test_group_fields: OK 💯✔️")

    def test_group_without_name(self) -> None:
        group = Group(**self.group_data_without_name)

        with self.assertRaises(ValidationError):
            group.full_clean()

        print("test_group_without_name: OK 💯✔️")

    def test_group_without_scientific_name(self) -> None:
        group = Group(**self.group_data_without_specific_name)

        with self.assertRaises(ValidationError):
            group.full_clean()

        print("test_group_without_scientific_name: OK 💯✔️")

    def test_one_group_for_many_animals(self):
        animals = [
            Animal.objects.create(
                **{
                    "name": "Beethoven",
                    "age": 1,
                    "weight": 30,
                    "sex": "Macho",
                    "group": self.group,
                }
            )
            for _ in range(20)
        ]

        for animal in animals:
            self.assertIs(animal.group, self.group)

        print("test_one_group_for_many_animals: OK 💯✔️")
