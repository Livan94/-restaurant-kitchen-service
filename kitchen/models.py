from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class Cook(AbstractUser):
    years_of_experience = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "cook"
        verbose_name_plural = "cooks"
        ordering = ["username"]

    def __str__(self) -> str:
        return f"{self.username} ({self.first_name} {self.last_name})"

    def get_absolute_url(self) -> str:
        return reverse("kitchen:cook-detail", args=[self.pk])


class DishType(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = "dish type"
        verbose_name_plural = "dish types"
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = "ingredient"
        verbose_name_plural = "ingredients"
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)

    dish_type = models.ForeignKey(
        DishType,
        on_delete=models.CASCADE,
        related_name="dishes",
    )
    cooks = models.ManyToManyField(
        Cook,
        related_name="dishes",
        blank=True,
    )
    ingredients = models.ManyToManyField(
        Ingredient,
        related_name="dishes",
        blank=True,
    )

    class Meta:
        verbose_name = "dish"
        verbose_name_plural = "dishes"
        ordering = ["name"]

    def __str__(self) -> str:
        return f"{self.name} (${self.price})"

    def get_absolute_url(self) -> str:
        return reverse("kitchen:dish-detail", args=[self.pk])
