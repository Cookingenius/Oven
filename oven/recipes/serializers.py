from rest_framework import serializers

from foods.serializers import FoodSerializer
from .models import Ingredient, Recipe, Step


class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Step
        fields = ('order', 'text', 'picture',)
        ordering = ('order',)


class IngredientSerializer(serializers.ModelSerializer):
    food = FoodSerializer()

    class Meta:
        model = Ingredient
        fields = ('order', 'quantity', 'food',)
        ordering = ('order',)


class RecipeSerializer(serializers.ModelSerializer):
    steps = StepSerializer(many=True)
    ingredients = IngredientSerializer(many=True)

    class Meta:
        model = Recipe
        fields = (
            'id',
            'title',
            'cooking_time',
            'preparation_time',
            'number_servings',
            'steps',
            'ingredients',
        )
