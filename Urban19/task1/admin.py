from django.contrib import admin
from .models import Buyer, Game

@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display = ('name', 'balance', 'age')  # Поля, которые будут отображаться в списке
    search_fields = ('name',)  # Поля для поиска

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'cost', 'size', 'age_limited')  # Поля для отображения
    search_fields = ('title',)  # Поля для поиска
    list_filter = ('age_limited',)  # Фильтрация по полям

