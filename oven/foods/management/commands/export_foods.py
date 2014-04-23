import json
import os

from django.core.management.base import BaseCommand, CommandError
from django.utils.text import slugify


from foods.models import Category
from foods.serializers import FoodSerializer


class Command(BaseCommand):
    args = '/path/to/export/directory/'
    help = 'Export the food db as json files (FoodDB format)'

    @staticmethod
    def get_food_data(category):
        foods = []

        for food in category.foods.all():
            food_data = FoodSerializer(food).data
            del(food_data['id'])
            del(food_data['category'])
            foods.append(food_data)

        return foods

    def handle(self, *args, **kwargs):
        if len(args) < 1:
            raise CommandError(
                'export_foods takes one argument.\n'
                'Example: "./manage.py export_foods /home/dean/FoodDB/"'
            )

        directory = args[0]

        for category in Category.objects.all():
            filename = '%s.json' % slugify(category.name)

            with open(os.path.join(directory, filename), 'w') as f:
                foods = self.get_food_data(category)
                data = {category.name: foods}
                json.dump(data, f, indent=4)
                print('Exported %s category containing %d foods' % (category.name, len(foods)))
