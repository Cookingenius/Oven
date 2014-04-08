from rest_framework import serializers

from .models import Food


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = (
            'id',
            'name',
            'category',
            'unitary',
            'unit_weight',
            'proteins',
            'carbs',
            'fat'
        )
