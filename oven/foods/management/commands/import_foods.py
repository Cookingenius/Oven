import json
import os

from django.core.management.base import BaseCommand, CommandError

from foods.models import Category, Food


class Command(BaseCommand):
    args = '/path/to/food_db/'
    help = 'Populate the Food table from food_db'

    @staticmethod
    def load_foods(foods, category):
        new_foods = 0

        for food in foods:
            _, created = Food.objects.update_or_create(
                name=food['name'],
                defaults={
                    'category': category,
                    'unit_weight': food['unit_weight'],
                    'proteins': food['proteins'],
                    'carbs': food['carbs'],
                    'fat': food['fat'],
                    'fat_saturated': food['fat_saturated'],
                    'fat_mono': food['fat_mono'],
                    'fat_poly': food['fat_poly'],
                    'sugar': food['sugar'],
                    'cholesterol': food['cholesterol'],
                    'fiber': food['fiber'],
                    'vitamin_a': food['vitamin_a'],
                    'vitamin_c': food['vitamin_c'],
                    'calcium': food['calcium'],
                    'iron': food['iron'],
                    'magnesium': food['magnesium'],
                    'potassium': food['potassium'],
                    'sodium': food['sodium'],
                }
            )
            if created:
                new_foods += 1

        return new_foods

    def handle(self, *args, **kwargs):
        if len(args) < 1:
            raise CommandError(
                'import_foods takes one argument.\n'
                'Example: "./manage.py import_foods /home/dean/FoodDB/"'
            )

        dir_walk = os.walk(args[0])
        new_foods_count = 0

        for dirpath, dirs, files in dir_walk:
            for filename in files:
                if not filename.endswith('.json'):
                    continue

                with open(os.path.join(dirpath, filename)) as f:
                    data = json.load(f)
                    category_name = list(data.keys())[0]

                    category, _ = Category.objects.get_or_create(name=category_name)
                    new_foods_count += self.load_foods(list(data.values())[0], category)

        print('You have inserted %d new foods! mmm... tasty!' % new_foods_count)

        return new_foods_count
