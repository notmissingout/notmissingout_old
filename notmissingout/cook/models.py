from django.db import models
from django import forms
from markdownx.models import MarkdownxField


class Recipe(models.Model):
    slug = models.SlugField(
        unique=True,
        help_text="Used to set the URL - will be based on the title initially",
    )

    title = models.TextField(
        help_text="Displayed as the heading for the recipe",
    )

    date = models.DateField(
        help_text="Date the recipe was completed. Used for ordering.",
    )

    cook = models.TextField(
        help_text="Name and description of the cook or cooks",
    )

    body = MarkdownxField(
        help_text="Body of the recipe, in markdown format.",
    )

    location = models.ForeignKey(
        'Location',
        help_text="The location that the recipe is associate with"
    )

    def __str__(self):
        return self.slug


class Flag(models.Model):
    name = models.TextField(
        help_text="Name of the flag",
    )

    image = models.ImageField(
        upload_to='flags',
        width_field='width',
        height_field='height',
        help_text='Image of the flag',
    )

    width = models.IntegerField()
    height = models.IntegerField()

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.TextField(
            help_text="Name of the location",
    )

    latitude = models.FloatField()
    longitude = models.FloatField()

    primary_flag = models.ForeignKey(
        'Flag',
        help_text='Main flag to display for the location',
        related_name='+',
    )

    secondary_flag = models.ForeignKey(
        'Flag',
        blank=True,
        null=True,
        help_text='Optional second flag to display for the location',
        related_name='+',
    )

    @property
    def fallback_flag(self):
        if self.secondary_flag:
            return self.secondary_flag
        return self.primary_flag

    def __str__(self):
        return '{} - {}:{}'.format(
            self.name,
            self.latitude,
            self.longitude,
        )
