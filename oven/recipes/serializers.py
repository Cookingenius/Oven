from rest_framework import serializers

from core.serializers import PictureSerializer
from foods.serializers import FoodSerializer
from .models import Ingredient, Recipe, Step


class IngredientSerializer(serializers.ModelSerializer):
    food = FoodSerializer()

    class Meta:
        model = Ingredient
        fields = ('order', 'quantity', 'food',)
        ordering = ('order',)


class StepSerializer(serializers.ModelSerializer):
    picture = PictureSerializer()

    class Meta:
        model = Step
        fields = ('order', 'text', 'picture',)
        ordering = ('order',)


class RecipeSerializer(serializers.ModelSerializer):
    picture = PictureSerializer()
    steps = StepSerializer(many=True)
    ingredients = IngredientSerializer(many=True)

    class Meta:
        model = Recipe
        fields = (
            'id',
            'name',
            'subtitle',
            'description',
            'picture',
            'cooking_time',
            'preparation_time',
            'number_servings',
            'steps',
            'ingredients',
        )
