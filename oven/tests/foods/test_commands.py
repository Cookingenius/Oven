from django.test import TestCase
from foods.management.commands import export_foods, import_foods
from foods.models import Food

from tests.factories._foods import CategoryFactory, FoodFactory


class ImportFoodTestCase(TestCase):

    def setUp(self):
        self.command = import_foods.Command()
        self.category = CategoryFactory()
        self.data = {
            self.category.name: [
                {
                    "name": "Chicken breast",
                    "unit_weight": 0.0,
                    "proteins": 33.4,
                    "carbs": 0.5,
                    "fat": 4.7,
                    "fat_saturated": 1.3,
                    "fat_mono": 1.7,
                    "fat_poly": 1.1,
                    "sugar": 0.0,
                    "cholesterol": 91.0,
                    "fiber": 0.0,
                    "vitamin_a": 23,
                    "vitamin_c": 0.0,
                    "calcium": 16,
                    "iron": 1.1,
                    "magnesium": 31,
                    "potassium": 276,
                    "sodium": 79.0
                }
            ]
        }

    def test_insert(self):
        self.command.load_foods(self.data[self.category.name], self.category)
        self.assertEqual(Food.objects.count(), len(self.data))
        self.assertEqual(
            Food.objects.filter(category=self.category).count(), len(self.data)
        )
        self.assertEqual(Food.objects.get().unit_weight, 0.0)

    def test_update(self):
        self.command.load_foods(self.data[self.category.name], self.category)
        self.data[self.category.name][0]['unit_weight'] = 50
        self.command.load_foods(self.data[self.category.name], self.category)
        self.assertEqual(Food.objects.get().unit_weight, 50)


class ExportFoodTestCase(TestCase):
    def setUp(self):
        self.food = FoodFactory()
        self.command = export_foods.Command()

    def test_get_food_data(self):
        data = self.command.get_food_data(self.food.category)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['name'], self.food.name)
