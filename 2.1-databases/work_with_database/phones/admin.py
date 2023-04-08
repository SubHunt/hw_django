from django.contrib import admin
from .models import Phone

"""Экспериментировал с получением из csv в бд, создалось много дубликатов за счет многократного перезапуска.
Удобней лишнее удалять через админку"""
@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'release_date', 'slug']
# Register your models here.
