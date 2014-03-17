from django.db import models

from model_utils.models import TimeStampedModel


class Food(TimeStampedModel):
    name = models.CharField(max_length=255)

    # macros for base unit of food (100g or unit)
    proteins = models.FloatField()
    carbs = models.FloatField()
    fat = models.FloatField()

    def __str__(self):
        return '%s' % self.name
