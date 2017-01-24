from django.contrib import admin

class SectionAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    fields = (
        'title',
        'slug',
        'parent',
    )
