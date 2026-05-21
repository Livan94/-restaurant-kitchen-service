from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Cook, Dish, DishType, Ingredient


def _apply_bootstrap(form):
    for field in form.fields.values():
        widget = field.widget

        if isinstance(widget, forms.CheckboxSelectMultiple):
            pass
        elif isinstance(widget, forms.SelectMultiple):
            widget.attrs.setdefault("class", "form-select")
        elif isinstance(widget, forms.Select):
            widget.attrs.setdefault("class", "form-select")
        elif isinstance(widget, forms.Textarea):
            widget.attrs.setdefault("class", "form-control")
        elif isinstance(widget, forms.CheckboxInput):
            widget.attrs.setdefault("class", "form-check-input")
        else:
            widget.attrs.setdefault("class", "form-control")

    return form



class CookCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Cook
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "years_of_experience",
            "password1",
            "password2",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        _apply_bootstrap(self)


class CookUpdateForm(forms.ModelForm):
    class Meta:
        model = Cook
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "years_of_experience",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        _apply_bootstrap(self)


class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = (
            "name",
            "description",
            "price",
            "dish_type",
            "cooks",
            "ingredients",
        )
        widgets = {
            "cooks": forms.CheckboxSelectMultiple,
            "ingredients": forms.CheckboxSelectMultiple,
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        _apply_bootstrap(self)


class DishTypeForm(forms.ModelForm):
    class Meta:
        model = DishType
        fields = ("name",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        _apply_bootstrap(self)


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ("name",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        _apply_bootstrap(self)


class SearchForm(forms.Form):
    query = forms.CharField(
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Search…",
            }
        ),
    )
