from django.contrib.contenttypes.fields import GenericRelation
from django.db import models

from model_utils.models import TimeStampedModel

from core.models import Picture
from foods.models import Food


class Recipe(TimeStampedModel):
    name = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=100)
    description = models.TextField()
    picture = GenericRelation(Picture, related_query_name='recipes')

    approved = models.BooleanField(default=False)

    # Times are in minutes
    cooking_time = models.IntegerField()
    preparation_time = models.IntegerField()

    number_servings = models.IntegerField()

    def __str__(self):
        return '%s' % self.name


class Ingredient(TimeStampedModel):
    recipe = models.ForeignKey(Recipe, related_name='ingredients')
    food = models.ForeignKey(Food)

    # In which order does it appear in the ingredient list
    order = models.IntegerField()

    quantity = models.FloatField()

    def __str__(self):
        return '%s for %s' % (self.food.name, self.recipe.name)


class Step(TimeStampedModel):
    recipe = models.ForeignKey(Recipe, related_name='steps')
    text = models.TextField()

    # Which step of the recipe this is
    order = models.IntegerField()

    picture = GenericRelation(
        Picture,
        related_query_name='steps', blank=True, null=True
    )

    def __str__(self):
        return '# %s for %s' % (str(self.order), self.recipe.name)
