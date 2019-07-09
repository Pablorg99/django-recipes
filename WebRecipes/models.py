from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField('Grams')

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    dinner_guests = models.PositiveIntegerField()
    ingredients = models.ManyToManyField(Ingredient)
    procedure = models.TextField('Instructions')
    publication_date = models.DateTimeField('Date Published')

    def __str__(self):
        return self.name
