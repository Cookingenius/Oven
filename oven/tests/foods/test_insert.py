from django.test import TestCase
from foods.management.commands import insert_macros
from foods.models import Food


class InsertTestCase(TestCase):

    def setUp(self):
        self.command = insert_macros.Command()
        self.category = 'delicious'
        self.data = {
            'Booger': {'weight': 5, 'carbs': 0, 'proteins': 2, 'fat': 0.2},
            'Chicken feet': {'carbs': 0, 'proteins': 19, 'fat': 15}
        }

    def test_insert(self):
        self.command.load_foods(self.data, self.category)
        self.assertEqual(Food.objects.count(), len(self.data))
        self.assertEqual(
            Food.objects.filter(category=self.category).count(), len(self.data)
        )
        self.assertEqual(Food.objects.get(unitary=True).unit_weight, 5.0)

    def test_update(self):
        self.command.load_foods(self.data, self.category)
        self.data['Booger']['weight'] = 4.5
        self.command.load_foods(self.data, self.category)
        self.assertEqual(Food.objects.get(name='Booger').unit_weight, 4.5)
