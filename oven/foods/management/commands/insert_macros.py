import json
import time
import os

from django.core.management.base import BaseCommand, CommandError

from foods.models import Food


class Command(BaseCommand):
    args = '/path/to/food_db/'
    help = 'Populate the Food table from food_db'

    def load_foods(self, foods, category):
        new_foods = 0

        for name, macros in foods.items():
            _, created = Food.objects.update_or_create(
                name=name,
                defaults={
                    'category': category,
                    'unitary': 'weight' in macros,
                    'unit_weight': macros.get('weight'),
                    'proteins': macros['proteins'],
                    'carbs': macros['carbs'],
                    'fat': macros['fat']
                }
            )
            if created:
                new_foods += 1

        return new_foods

    def handle(self, *args, **kwargs):
        if len(args) < 1:
            raise CommandError(
                'load_macros takes one argument.\n'
                'Example: "./manage.py load_macros /home/dean/FoodDB/"'
            )

        dir_walk = os.walk(args[0])
        new_foods = 0
        
        for dirpath, dirs, files in dir_walk:
            for filename in files:
                if not filename.endswith('.json'):
                    continue

                with open(os.path.join(dirpath, filename)) as f:
                    new_foods += self.load_foods(
                        json.loads(f.read()), filename.split('.json')[0]
                    )

        print('You have inserted %d new foods! mmm... tasty!' % new_foods)

