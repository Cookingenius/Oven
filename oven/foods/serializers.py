from rest_framework import serializers

from .models import Category, Food


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'name',
        )


class FoodSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Food
        fields = (
            'id',
            'name',
            'category',
            'unit_weight',
            'proteins',
            'carbs',
            'fat',
            'fat_saturated',
            'fat_mono',
            'fat_poly',
            'sugar',
            'cholesterol',
            'fiber',
            'vitamin_a',
            'vitamin_c',
            'calcium',
            'iron',
            'magnesium',
            'potassium',
            'sodium',
        )
