from django.core.management.base import CommandError
from django.test import TestCase

from core.management.commands import bootstrap
from recipes.models import Recipe, Ingredient, Step

from tests.factories._foods import FoodFactory


class BootstrapTestCase(TestCase):
    def setUp(self):
        self.command = bootstrap.Command()

    def test_create_recipe(self):
        self.command._create_recipe('Chicken', [FoodFactory()])

        self.assertEqual(Recipe.objects.count(), 1)
        self.assertEqual(Ingredient.objects.count(), 1)
        self.assertEqual(Step.objects.count(), 3)
