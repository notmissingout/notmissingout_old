from .models import Article, Section
from common import HtmlField
from django import forms
from django.contrib import admin
from django.db import models
from mptt.admin import DraggableMPTTAdmin


class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title", )}

    formfield_overrides = {
        models.TextField: {
            'widget': forms.TextInput(attrs={'size': '60'})
        },
    }

    fields = (
        'title',
        'slug',
        'section',
        'body',
    )
    readonly_fields = ('url', )


class SectionAdmin(DraggableMPTTAdmin):
    prepopulated_fields = {"slug": ("title", )}

    formfield_overrides = {
        models.TextField: {
            'widget': forms.TextInput(attrs={'size': '60'})
        },
    }

    fields = (
        'title',
        'slug',
        'parent',
    )

    list_display = (
        'tree_actions',
        'indented_title',
        'url',
    )
    list_display_links = ('indented_title', )


admin.site.register(Article, ArticleAdmin)
admin.site.register(Section, SectionAdmin)
