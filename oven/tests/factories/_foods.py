import factory

from foods.models import Category, Food


class CategoryFactory(factory.DjangoModelFactory):
    FACTORY_FOR = Category

    name = 'Meat'


class FoodFactory(factory.DjangoModelFactory):
    FACTORY_FOR = Food

    name = 'Chicken Breast'
    category = factory.SubFactory(CategoryFactory)

    unit_weight = 0
    proteins = 20.5
    carbs = 3.6
    fat = 1.1

    fat_saturated = 0
    fat_mono = 0
    fat_poly = 0
    sugar = 0
    cholesterol = 10
    fiber = 0

    vitamin_a = 40
    vitamin_c = 1.1

    calcium = 20
    iron = 1.2
    magnesium = 240
    potassium = 60
