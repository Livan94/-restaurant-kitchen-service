from django import forms
from django.test import TestCase

from kitchen.forms import (
    CookCreationForm,
    CookSearchForm,
    CookUpdateForm,
    DishForm,
    DishSearchForm,
    DishTypeForm,
    DishTypeSearchForm,
    IngredientForm,
    IngredientSearchForm,
)
from kitchen.models import Cook, DishType, Ingredient


class FormTests(TestCase):
    def setUp(self):
        self.cook = Cook.objects.create_user(
            username="chef_ivan",
            password="testpass123",
        )
        self.dish_type = DishType.objects.create(name="Main course")
        self.ingredient = Ingredient.objects.create(name="Salt")

    def test_cook_creation_form_fields_have_bootstrap_class(self):
        form = CookCreationForm()
        self.assertEqual(form.fields["username"].widget.attrs["class"], "form-control")
        self.assertEqual(form.fields["first_name"].widget.attrs["class"], "form-control")
        self.assertEqual(form.fields["last_name"].widget.attrs["class"], "form-control")
        self.assertEqual(form.fields["email"].widget.attrs["class"], "form-control")
        self.assertEqual(
            form.fields["years_of_experience"].widget.attrs["class"],
            "form-control",
        )

    def test_cook_update_form_fields_have_bootstrap_class(self):
        form = CookUpdateForm()
        self.assertEqual(form.fields["username"].widget.attrs["class"], "form-control")
        self.assertEqual(
            form.fields["years_of_experience"].widget.attrs["class"],
            "form-control",
        )

    def test_dish_form_uses_checkbox_select_multiple_widgets(self):
        form = DishForm()
        self.assertIsInstance(form.fields["cooks"].widget, forms.CheckboxSelectMultiple)
        self.assertIsInstance(
            form.fields["ingredients"].widget,
            forms.CheckboxSelectMultiple,
        )

    def test_dish_form_other_fields_have_bootstrap_classes(self):
        form = DishForm()
        self.assertEqual(form.fields["name"].widget.attrs["class"], "form-control")
        self.assertEqual(
            form.fields["description"].widget.attrs["class"],
            "form-control",
        )
        self.assertEqual(form.fields["price"].widget.attrs["class"], "form-control")
        self.assertEqual(form.fields["dish_type"].widget.attrs["class"], "form-select")

    def test_dish_type_form_has_bootstrap_class(self):
        form = DishTypeForm()
        self.assertEqual(form.fields["name"].widget.attrs["class"], "form-control")

    def test_ingredient_form_has_bootstrap_class(self):
        form = IngredientForm()
        self.assertEqual(form.fields["name"].widget.attrs["class"], "form-control")

    def test_cook_search_form_placeholder(self):
        form = CookSearchForm()
        self.assertEqual(
            form.fields["query"].widget.attrs["placeholder"],
            "🔎︎ Search by username...",
        )

    def test_dish_search_form_placeholder(self):
        form = DishSearchForm()
        self.assertEqual(
            form.fields["query"].widget.attrs["placeholder"],
            "🔎︎ Search by dish name...",
        )

    def test_dish_type_search_form_placeholder(self):
        form = DishTypeSearchForm()
        self.assertEqual(
            form.fields["query"].widget.attrs["placeholder"],
            "🔎︎ Search by category name...",
        )

    def test_ingredient_search_form_placeholder(self):
        form = IngredientSearchForm()
        self.assertEqual(
            form.fields["query"].widget.attrs["placeholder"],
            "🔎︎ Search by ingredient...",
        )
