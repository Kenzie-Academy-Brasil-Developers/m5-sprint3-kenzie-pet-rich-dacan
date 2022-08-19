from animals.models import Animal
from django.test import TestCase
from groups.models import Group
from traits.models import Trait


class AnimalModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:

        cls.animal_test1_data = {
            "name": "Beethoven",
            "age": 10,
            "weight": 12.45,
            "sex": "Macho",
            # "group": {"name": "gato", "scientific_name": "felis catus"},
            # "traits": [{"name": "pelo curto"}, {"name": "pequeno porte"}],
        }

        # cls.animal_test2_data = {
        #     "name": "Beethoven",
        #     "age": 10,
        #     "weight": 12.45,
        #     "group": {"name": "gato", "scientific_name": "felis catus"},
        #     "traits": [{"name": "pelo curto"}, {"name": "pequeno porte"}],
        # }

        # cls.animal_test3_data = {
        #     "name": "Beethoven",
        #     "age": 10,
        #     "weight": 12.45,
        #     "sex": "Não Identificado",
        #     "group": {"name": "gato", "scientific_name": "felis catus"},
        #     "traits": [{"name": "pelo curto"}, {"name": "pequeno porte"}],
        # }

        cls.animal_test1 = Animal.objects.create(**cls.animal_test1_data)

        group_1_test = {"name": "gato", "scientific_name": "felis catus"}

        cls.group_1 = Group(**group_1_test)

        traits_1_test = [{"name": "pelo curto"}, {"name": "pequeno porte"}]

        cls.traits_1 = Trait(**traits_1_test)

        # cls.animal_test2 = Animal.objects.create(**cls.animal_test2_data)

    def test_animal_fields(self):
        print(self.animal_test1)
