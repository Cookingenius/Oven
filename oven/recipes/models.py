from django.db import models

from model_utils.models import TimeStampedModel

from foods.models import Food


class Recipe(TimeStampedModel):
    title = models.CharField(max_length=255)
    approved = models.BooleanField(default=False)

    # Times are in minutes
    cooking_time = models.IntegerField()
    preparation_time = models.IntegerField()

    number_servings = models.IntegerField()

    def __str__(self):
        return '%s' % self.title


class Picture(TimeStampedModel):
    recipe = models.ForeignKey(Recipe, related_name='picture')
    url = models.CharField(max_length=700)


class Ingredient(TimeStampedModel):
    recipe = models.ForeignKey(Recipe, related_name='ingredients')
    food = models.ForeignKey(Food)

    # In which order does it appear in the ingredient list
    order = models.IntegerField()

    quantity = models.FloatField()

    def __str__(self):
        return '%s for %s' % (self.food.name, self.recipe.title)


class Step(TimeStampedModel):
    recipe = models.ForeignKey(Recipe, related_name='steps')
    text = models.TextField()

    # Which step of the recipe this is
    order = models.IntegerField()

    picture = models.ForeignKey(Picture, blank=True, null=True)

    def __str__(self):
        return '# %s for %s' % (str(self.number), self.recipe.title)
