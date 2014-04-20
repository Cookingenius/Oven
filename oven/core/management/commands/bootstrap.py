from os.path import dirname

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from foods.models import Food
from foods.management.commands import import_foods
from recipes.models import Ingredient, Recipe, Step


class Command(BaseCommand):
    """
    Bootstraps a completely new database:
      - inserts foods using FoodDB submodule
      - inserts recipes using these foods
    """
    help = __doc__

    def _create_recipe(self, name, foods, cooking_time=0, preparation_time=0):
        """
        Creates a recipe with the given parameters and adds some bogus steps
        """
        recipe = Recipe(
            name=name,
            cooking_time=cooking_time,
            preparation_time=preparation_time,
            approved=True,
            number_servings=2
        )
        recipe.save()

        for index, food in enumerate(foods):
            recipe.ingredients.add(
                Ingredient(quantity=1, food=food, order=index, recipe=recipe)
            )

        recipe.steps.add(
            Step(order=1, text="Step 1 blabla", recipe=recipe),
            Step(order=2, text="Step 2 blabla", recipe=recipe),
            Step(order=3, text="Step 3 blabla", recipe=recipe),
        )

        recipe.save()

    def handle(self, *args, **kwargs):
        # Getting rid of the current db
        print("Deleting current objects in the db")
        Recipe.objects.all().delete()
        Food.objects.all().delete()

        # Re-inserting foods
        print("Importing foods from FoodDB")
        inserted_count = import_foods.Command().handle(
            '%s/FoodDB' % dirname(settings.SITE_ROOT)
        )

        if inserted_count == 0:
            raise CommandError(
                "No food was inserted."
                "Did you update the submodules for FoodDB?"
            )

        print("Creating recipes")
        self._create_recipe('Spicy chicken breasts', [
            Food.objects.get(name='Chicken breast'),
            Food.objects.get(name='Paprika'),
            Food.objects.get(name='Black pepper'),
            Food.objects.get(name='Olive oil'),
        ], cooking_time=50, preparation_time=20)

        self._create_recipe('Tropical smoothie', [
            Food.objects.get(name='Mango'),
            Food.objects.get(name='Apple'),
            Food.objects.get(name='Pineapple'),
            Food.objects.get(name='Nectarine'),
            Food.objects.get(name='Guava'),
            Food.objects.get(name='Banana'),
        ])

        print("Done!")
