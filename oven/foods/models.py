from django.db import models

from model_utils.models import TimeStampedModel


class Category(TimeStampedModel):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return '%s' % self.name


class Food(TimeStampedModel):
    name = models.CharField(max_length=255, unique=True)
    category = models.ForeignKey(Category, related_name='foods')

    unit_weight = models.IntegerField(
        blank=True, null=True,
        help_text='Average weight of a base unit (grams)'
    )

    # macros for 100g
    proteins = models.FloatField(default=0)
    carbs = models.FloatField(default=0)
    fat = models.FloatField(default=0)

    # details fat/sugar/etc for 100g
    fat_saturated = models.FloatField(default=0)
    fat_mono = models.FloatField(default=0)
    fat_poly = models.FloatField(default=0)
    sugar = models.FloatField(default=0)
    cholesterol = models.IntegerField(default=0)
    fiber = models.FloatField(default=0)

    # vitamins for 100g
    vitamin_a = models.IntegerField(default=0)
    vitamin_c = models.FloatField(default=0)

    # minerals for 100g
    calcium = models.IntegerField(default=0)
    iron = models.FloatField(default=0)
    magnesium = models.IntegerField(default=0)
    potassium = models.IntegerField(default=0)
    sodium = models.FloatField(default=0)

    def __str__(self):
        return '%s' % self.name

