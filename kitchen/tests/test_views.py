from decimal import Decimal

from django.test import TestCase
from django.urls import reverse

from kitchen.forms import (
    CookSearchForm,
    DishSearchForm,
    DishTypeSearchForm,
    IngredientSearchForm,
)
from kitchen.models import Cook, Dish, DishType, Ingredient


class PublicViewTests(TestCase):
    def test_login_required_for_index(self):
        response = self.client.get(reverse("kitchen:index"))
        self.assertNotEqual(response.status_code, 200)

    def test_login_required_for_cook_list(self):
        response = self.client.get(reverse("kitchen:cook-list"))
        self.assertNotEqual(response.status_code, 200)

    def test_login_required_for_dish_list(self):
        response = self.client.get(reverse("kitchen:dish-list"))
        self.assertNotEqual(response.status_code, 200)

    def test_login_required_for_dish_type_list(self):
        response = self.client.get(reverse("kitchen:dish-type-list"))
        self.assertNotEqual(response.status_code, 200)

    def test_login_required_for_ingredient_list(self):
        response = self.client.get(reverse("kitchen:ingredient-list"))
        self.assertNotEqual(response.status_code, 200)

    def test_login_required_for_cook_create(self):
        response = self.client.get(reverse("kitchen:cook-create"))
        self.assertRedirects(
            response,
            f"{reverse('login')}?next={reverse('kitchen:cook-create')}",
        )



class PrivateViewTests(TestCase):
    def setUp(self):
        self.user = Cook.objects.create_user(
            username="admin_user",
            password="testpass123",
            first_name="Admin",
            last_name="User",
            years_of_experience=10,
        )
        self.client.force_login(self.user)

        self.other_cook = Cook.objects.create_user(
            username="chef_olena",
            password="testpass123",
            first_name="Olena",
            last_name="Petrenko",
            years_of_experience=7,
        )

        self.dessert = DishType.objects.create(name="Dessert")
        self.drink = DishType.objects.create(name="Drink")

        self.sugar = Ingredient.objects.create(name="Sugar")
        self.salt = Ingredient.objects.create(name="Salt")

        self.cheesecake = Dish.objects.create(
            name="Cheesecake",
            description="Creamy dessert",
            price=Decimal("12.50"),
            dish_type=self.dessert,
        )
        self.coffee = Dish.objects.create(
            name="Coffee",
            description="Hot drink",
            price=Decimal("4.00"),
            dish_type=self.drink,
        )

        self.cheesecake.cooks.add(self.user)
        self.cheesecake.ingredients.add(self.sugar)
        self.coffee.cooks.add(self.other_cook)
        self.coffee.ingredients.add(self.salt)

    def test_index_view_status_code(self):
        response = self.client.get(reverse("kitchen:index"))
        self.assertEqual(response.status_code, 200)

    def test_index_view_uses_correct_template(self):
        response = self.client.get(reverse("kitchen:index"))
        self.assertTemplateUsed(response, "kitchen/index.html")

    def test_index_view_contains_statistics(self):
        response = self.client.get(reverse("kitchen:index"))
        self.assertEqual(response.context["num_dishes"], 2)
        self.assertEqual(response.context["num_cooks"], 2)
        self.assertEqual(response.context["num_dish_types"], 2)
        self.assertEqual(response.context["num_ingredients"], 2)

    def test_index_view_increments_num_visits(self):
        first_response = self.client.get(reverse("kitchen:index"))
        second_response = self.client.get(reverse("kitchen:index"))

        self.assertEqual(first_response.context["num_visits"], 1)
        self.assertEqual(second_response.context["num_visits"], 2)

    def test_cook_list_view_uses_correct_search_form(self):
        response = self.client.get(reverse("kitchen:cook-list"))
        self.assertIsInstance(response.context["search_form"], CookSearchForm)

    def test_cook_list_view_filters_by_username(self):
        response = self.client.get(
            reverse("kitchen:cook-list"),
            {"query": "olena"},
        )
        cooks = list(response.context["cook_list"])
        self.assertEqual(cooks, [self.other_cook])

    def test_dish_list_view_uses_correct_search_form(self):
        response = self.client.get(reverse("kitchen:dish-list"))
        self.assertIsInstance(response.context["search_form"], DishSearchForm)

    def test_dish_list_view_filters_by_name(self):
        response = self.client.get(
            reverse("kitchen:dish-list"),
            {"query": "Cheese"},
        )
        dishes = list(response.context["dish_list"])
        self.assertEqual(dishes, [self.cheesecake])

    def test_dish_type_list_view_uses_correct_search_form(self):
        response = self.client.get(reverse("kitchen:dish-type-list"))
        self.assertIsInstance(response.context["search_form"], DishTypeSearchForm)

    def test_dish_type_list_view_filters_by_name(self):
        response = self.client.get(
            reverse("kitchen:dish-type-list"),
            {"query": "Dess"},
        )
        dish_types = list(response.context["dish_type_list"])
        self.assertEqual(dish_types, [self.dessert])

    def test_ingredient_list_view_uses_correct_search_form(self):
        response = self.client.get(reverse("kitchen:ingredient-list"))
        self.assertIsInstance(response.context["search_form"], IngredientSearchForm)

    def test_ingredient_list_view_filters_by_name(self):
        response = self.client.get(
            reverse("kitchen:ingredient-list"),
            {"query": "Sug"},
        )
        ingredients = list(response.context["ingredient_list"])
        self.assertEqual(ingredients, [self.sugar])

    def test_dish_detail_view_status_code(self):
        response = self.client.get(
            reverse("kitchen:dish-detail", args=[self.cheesecake.pk])
        )
        self.assertEqual(response.status_code, 200)

    def test_cook_detail_view_status_code(self):
        response = self.client.get(
            reverse("kitchen:cook-detail", args=[self.user.pk])
        )
        self.assertEqual(response.status_code, 200)

    def test_dish_create_view_status_code(self):
        response = self.client.get(reverse("kitchen:dish-create"))
        self.assertEqual(response.status_code, 200)

    def test_dish_type_create_view_status_code(self):
        response = self.client.get(reverse("kitchen:dish-type-create"))
        self.assertEqual(response.status_code, 200)

    def test_ingredient_create_view_status_code(self):
        response = self.client.get(reverse("kitchen:ingredient-create"))
        self.assertEqual(response.status_code, 200)

    def test_cook_create_view_status_code(self):
        response = self.client.get(reverse("kitchen:cook-create"))
        self.assertEqual(response.status_code, 200)
