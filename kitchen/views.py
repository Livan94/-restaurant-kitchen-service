from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    TemplateView,
    UpdateView,
)

from .forms import (
    CookCreationForm,
    CookUpdateForm,
    DishForm,
    DishTypeForm,
    IngredientForm,
    CookSearchForm,
    DishSearchForm,
    DishTypeSearchForm,
    IngredientSearchForm,
)
from .models import Cook, Dish, DishType, Ingredient


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = "kitchen/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        num_visits = self.request.session.get("num_visits", 0) + 1
        self.request.session["num_visits"] = num_visits
        context["num_visits"] = num_visits
        context["num_dishes"] = Dish.objects.count()
        context["num_cooks"] = Cook.objects.count()
        context["num_dish_types"] = DishType.objects.count()
        context["num_ingredients"] = Ingredient.objects.count()
        return context


class DishTypeListView(LoginRequiredMixin, ListView):
    model = DishType
    template_name = "kitchen/dish_type_list.html"
    context_object_name = "dish_type_list"
    paginate_by = 5

    def get_queryset(self):
        queryset = DishType.objects.all()
        query = self.request.GET.get("query", "").strip()
        if query:
            queryset = queryset.filter(name__icontains=query)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_form"] = DishTypeSearchForm(self.request.GET or None)
        context["query"] = self.request.GET.get("query", "")
        return context


class DishTypeCreateView(LoginRequiredMixin, CreateView):
    model = DishType
    form_class = DishTypeForm
    template_name = "kitchen/dish_type_form.html"
    success_url = reverse_lazy("kitchen:dish-type-list")


class DishTypeUpdateView(LoginRequiredMixin, UpdateView):
    model = DishType
    form_class = DishTypeForm
    template_name = "kitchen/dish_type_form.html"
    success_url = reverse_lazy("kitchen:dish-type-list")


class DishTypeDeleteView(LoginRequiredMixin, DeleteView):
    model = DishType
    template_name = "kitchen/dish_type_confirm_delete.html"
    success_url = reverse_lazy("kitchen:dish-type-list")


class IngredientListView(LoginRequiredMixin, ListView):
    model = Ingredient
    template_name = "kitchen/ingredient_list.html"
    context_object_name = "ingredient_list"
    paginate_by = 5

    def get_queryset(self):
        queryset = Ingredient.objects.all()
        query = self.request.GET.get("query", "").strip()
        if query:
            queryset = queryset.filter(name__icontains=query)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_form"] = IngredientSearchForm(self.request.GET or None)
        context["query"] = self.request.GET.get("query", "")
        return context


class IngredientCreateView(LoginRequiredMixin, CreateView):
    model = Ingredient
    form_class = IngredientForm
    template_name = "kitchen/ingredient_form.html"
    success_url = reverse_lazy("kitchen:ingredient-list")


class IngredientUpdateView(LoginRequiredMixin, UpdateView):
    model = Ingredient
    form_class = IngredientForm
    template_name = "kitchen/ingredient_form.html"
    success_url = reverse_lazy("kitchen:ingredient-list")


class IngredientDeleteView(LoginRequiredMixin, DeleteView):
    model = Ingredient
    template_name = "kitchen/ingredient_confirm_delete.html"
    success_url = reverse_lazy("kitchen:ingredient-list")


class DishListView(LoginRequiredMixin, ListView):
    model = Dish
    template_name = "kitchen/dish_list.html"
    context_object_name = "dish_list"
    paginate_by = 5

    def get_queryset(self):
        queryset = Dish.objects.select_related("dish_type")
        query = self.request.GET.get("query", "").strip()
        if query:
            queryset = queryset.filter(name__icontains=query)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_form"] = DishSearchForm(self.request.GET or None)
        context["query"] = self.request.GET.get("query", "")
        return context


class DishDetailView(LoginRequiredMixin, DetailView):
    model = Dish
    template_name = "kitchen/dish_detail.html"
    queryset = Dish.objects.select_related(
        "dish_type"
    ).prefetch_related("cooks", "ingredients")


class DishCreateView(LoginRequiredMixin, CreateView):
    model = Dish
    form_class = DishForm
    template_name = "kitchen/dish_form.html"


class DishUpdateView(LoginRequiredMixin, UpdateView):
    model = Dish
    form_class = DishForm
    template_name = "kitchen/dish_form.html"


class DishDeleteView(LoginRequiredMixin, DeleteView):
    model = Dish
    template_name = "kitchen/dish_confirm_delete.html"
    success_url = reverse_lazy("kitchen:dish-list")


class CookListView(LoginRequiredMixin, ListView):
    model = Cook
    template_name = "kitchen/cook_list.html"
    context_object_name = "cook_list"
    paginate_by = 5

    def get_queryset(self):
        queryset = Cook.objects.all()
        query = self.request.GET.get("query", "").strip()
        if query:
            queryset = queryset.filter(username__icontains=query)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_form"] = CookSearchForm(self.request.GET or None)
        context["query"] = self.request.GET.get("query", "")
        return context


class CookDetailView(LoginRequiredMixin, DetailView):
    model = Cook
    template_name = "kitchen/cook_detail.html"
    queryset = Cook.objects.prefetch_related("dishes__dish_type")


class CookCreateView(CreateView):
    model = Cook
    form_class = CookCreationForm
    template_name = "kitchen/cook_form.html"
    success_url = reverse_lazy("kitchen:cook-list")


class CookUpdateView(LoginRequiredMixin, UpdateView):
    model = Cook
    form_class = CookUpdateForm
    template_name = "kitchen/cook_form.html"


class CookDeleteView(LoginRequiredMixin, DeleteView):
    model = Cook
    template_name = "kitchen/cook_confirm_delete.html"
    success_url = reverse_lazy("kitchen:cook-list")
