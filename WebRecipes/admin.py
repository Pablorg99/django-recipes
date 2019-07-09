from django.contrib import admin

from .models import Recipe
from .models import Ingredient

admin.site.register(Recipe)
admin.site.register(Ingredient)