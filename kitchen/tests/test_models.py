from decimal import Decimal

from django.test import TestCase
from django.urls import reverse

from kitchen.models import Cook, Dish, DishType, Ingredient


class ModelTests(TestCase):
    def setUp(self):
        self.cook = Cook.objects.create_user(
            username="chef_anna",
            password="testpass123",
            first_name="Anna",
            last_name="Kravets",
            years_of_experience=5,
        )
        self.dish_type = DishType.objects.create(name="Dessert")
        self.ingredient = Ingredient.objects.create(name="Sugar")
        self.dish = Dish.objects.create(
            name="Cheesecake",
            description="Creamy dessert",
            price=Decimal("12.50"),
            dish_type=self.dish_type,
        )
        self.dish.cooks.add(self.cook)
        self.dish.ingredients.add(self.ingredient)

    def test_cook_str(self):
        self.assertEqual(str(self.cook), "chef_anna (Anna Kravets)")

    def test_cook_get_absolute_url(self):
        self.assertEqual(
            self.cook.get_absolute_url(),
            reverse("kitchen:cook-detail", args=[self.cook.pk]),
        )

    def test_cook_meta_ordering(self):
        self.assertEqual(Cook._meta.ordering, ["username"])

    def test_dish_type_str(self):
        self.assertEqual(str(self.dish_type), "Dessert")

    def test_dish_type_meta_ordering(self):
        self.assertEqual(DishType._meta.ordering, ["name"])

    def test_ingredient_str(self):
        self.assertEqual(str(self.ingredient), "Sugar")

    def test_ingredient_meta_ordering(self):
        self.assertEqual(Ingredient._meta.ordering, ["name"])

    def test_dish_str(self):
        self.assertEqual(str(self.dish), "Cheesecake ($12.50)")

    def test_dish_get_absolute_url(self):
        self.assertEqual(
            self.dish.get_absolute_url(),
            reverse("kitchen:dish-detail", args=[self.dish.pk]),
        )

    def test_dish_meta_ordering(self):
        self.assertEqual(Dish._meta.ordering, ["name"])
