from django.db import models


class Ingredient(models.Model):
    name: str = models.CharField(max_length=50)
    quantity: int = models.PositiveIntegerField('Grams')

    def __str__(self):
        return str(self.quantity) + "g " + self.name


class Recipe(models.Model):
    name: str = models.CharField(max_length=100)
    dinner_guests: int = models.PositiveIntegerField()
    ingredients = models.ManyToManyField(Ingredient)
    procedure: str = models.TextField('Instructions')
    publication_date = models.DateTimeField('Date Published')

    def __str__(self):
        return self.name
