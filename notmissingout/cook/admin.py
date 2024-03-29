from .models import Recipe, Location, Flag
from common import HtmlField
from django import forms
from django.contrib import admin
from django.db import models
from mediumeditor.admin import MediumEditorAdmin


class RecipeAdmin(admin.ModelAdmin):
    date_heirarchy = 'date'
    prepopulated_fields = {"slug": ("title",)}

    formfield_overrides = {
        models.TextField: {'widget': forms.TextInput(attrs={'size': '60'})},
    }

    fields = (
        'title',
        'slug',
        'date',
        'cook',
        'body',
        'location',
    )


class LocationAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': forms.TextInput(attrs={'size': '40'})},
    }

    fields = (
        'name',
        (
            'latitude',
            'longitude',
        ),
        'primary_flag',
        'secondary_flag',
    )


class FlagAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': forms.TextInput(attrs={'size': '40'})},
    }

    readonly_fields = (
        'width',
        'height',
    )


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Flag, FlagAdmin)
