from django.contrib import admin
from django.test import TestCase

from kitchen.admin import CookAdmin, DishAdmin, DishTypeAdmin, IngredientAdmin
from kitchen.models import Cook, Dish, DishType, Ingredient


class AdminTests(TestCase):
    def test_models_are_registered_in_admin(self):
        self.assertIn(Cook, admin.site._registry)
        self.assertIn(DishType, admin.site._registry)
        self.assertIn(Ingredient, admin.site._registry)
        self.assertIn(Dish, admin.site._registry)

    def test_cook_admin_configuration(self):
        model_admin = admin.site._registry[Cook]
        self.assertIsInstance(model_admin, CookAdmin)
        self.assertIn("years_of_experience", model_admin.list_display)

        fieldsets_fields = []
        for _, options in model_admin.fieldsets:
            fieldsets_fields.extend(options.get("fields", []))
        self.assertIn("years_of_experience", fieldsets_fields)

        add_fieldsets_fields = []
        for _, options in model_admin.add_fieldsets:
            add_fieldsets_fields.extend(options.get("fields", []))
        self.assertIn("years_of_experience", add_fieldsets_fields)

    def test_dish_type_admin_configuration(self):
        model_admin = admin.site._registry[DishType]
        self.assertIsInstance(model_admin, DishTypeAdmin)
        self.assertEqual(model_admin.list_display, ("name",))
        self.assertEqual(model_admin.search_fields, ("name",))
        self.assertEqual(model_admin.ordering, ("name",))

    def test_ingredient_admin_configuration(self):
        model_admin = admin.site._registry[Ingredient]
        self.assertIsInstance(model_admin, IngredientAdmin)
        self.assertEqual(model_admin.list_display, ("name",))
        self.assertEqual(model_admin.search_fields, ("name",))
        self.assertEqual(model_admin.ordering, ("name",))

    def test_dish_admin_configuration(self):
        model_admin = admin.site._registry[Dish]
        self.assertIsInstance(model_admin, DishAdmin)
        self.assertEqual(model_admin.list_display,
                         ("name", "price", "dish_type")
                         )
        self.assertEqual(model_admin.list_filter, ("dish_type",))
        self.assertEqual(model_admin.search_fields, ("name",))
        self.assertEqual(model_admin.filter_horizontal,
                         ("cooks", "ingredients")
                         )
