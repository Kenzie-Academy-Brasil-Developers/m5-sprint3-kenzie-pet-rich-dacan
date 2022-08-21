from animals.models import Animal
from django.core.exceptions import ValidationError
from django.test import TestCase
from groups.models import Group
from traits.models import Trait


class AnimalModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:

        cls.default_animal_sex = "Não Informado"

        cls.animal_test_correct_data = {
            "name": "Beethoven",
            "age": 10,
            "weight": 12.45,
            "sex": "Macho",
        }

        cls.animal_test_sexless = {
            "name": "Ragnar",
            "age": 10,
            "weight": 12.45,
        }

        cls.animal_test_sex_incorrect = {
            "name": "Beethoven",
            "age": 10,
            "weight": 12.45,
            "sex": "Não Identificado",
        }

        # Instanciando animais
        cls.animal_test1 = Animal(**cls.animal_test_correct_data)
        cls.animal_test2 = Animal(**cls.animal_test_sexless)
        cls.animal_test3 = Animal(**cls.animal_test_sex_incorrect)

        # Instanciando grupos
        cls.group_1_data = {"name": "cão", "scientific_name": "canis familiaris"}
        cls.group_1 = Group.objects.create(**cls.group_1_data)

        cls.group_2_data = {"name": "gato", "scientific_name": "felis catus"}
        cls.group_2 = Group.objects.create(**cls.group_2_data)

        # Instanciando traits
        cls.trait_1_data = {"name": "pequeno porte"}
        cls.trait_1 = Trait.objects.create(**cls.trait_1_data)

        cls.trait_2_data = {"name": "pelo curto"}
        cls.trait_2 = Trait.objects.create(**cls.trait_2_data)

        cls.traits_list = [cls.trait_1, cls.trait_2]

    def test_animal_fields(self) -> None:

        self.animal_test1.group = self.group_1
        self.animal_test1.save()

        self.assertEqual(
            self.animal_test1.group, self.group_1, "Verify group attribute."
        )
        self.assertEqual(
            self.animal_test1.name,
            self.animal_test_correct_data["name"],
            "Verify name attribute.",
        )
        self.assertEqual(
            self.animal_test1.age,
            self.animal_test_correct_data["age"],
            "Verify age attribute.",
        )
        self.assertEqual(
            self.animal_test1.weight,
            self.animal_test_correct_data["weight"],
            "Verify weight attribute.",
        )
        self.assertEqual(
            self.animal_test1.sex,
            self.animal_test_correct_data["sex"],
            "Verify sex attribute.",
        )

        print("test_animal_fields: OK 💯✔️")

    def test_animal_without_group(self):

        with self.assertRaises(ValidationError):
            self.animal_test1.full_clean()

        print("test_animal_without_group: OK 💯✔️")

    def test_sex_attribute_incorrect(self) -> None:

        self.animal_test3.group = self.group_2
        self.animal_test3.save()

        # capturando exceções com o with
        # with self.assertRaises(ValidationError):
        #     self.animal_test3.full_clean()

        self.assertRaises(ValidationError, self.animal_test3.full_clean)

        print("test_sex_attribute_incorrect: OK 💯✔️")

    def test_sex_attribute_not_informed(self) -> None:

        msg = f"Verifique se o valor para `sex` igual à : {self.default_animal_sex}"

        self.assertEqual(self.animal_test2.sex, self.default_animal_sex, msg)

        print("test_sex_attribute_not_informed: OK 💯✔️")
