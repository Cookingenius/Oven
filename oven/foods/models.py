from django.db import models

from model_utils.models import TimeStampedModel


class Food(TimeStampedModel):
    name = models.CharField(max_length=255, unique=True)
    category = models.CharField(max_length=255, blank=True, null=True)

    unitary = models.BooleanField(
        default=False,
        help_text='True if the macros are for a base unit'
    )
    unit_weight = models.FloatField(
        blank=True, null=True,
        help_text='Average weight of a base unit (grams)'
    )

    # macros for base unit of food (100g or unit)
    proteins = models.FloatField()
    carbs = models.FloatField()
    fat = models.FloatField()

    def __str__(self):
        return '%s' % self.name
