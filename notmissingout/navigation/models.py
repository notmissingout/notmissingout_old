from django.db import models
from common import HtmlField


class Article(models.Model):
    title = models.TextField(
        help_text="Displayed as the title for the article",
    )

    slug = models.SlugField(
        help_text="Used to set the URL - will be based on the title initially",
    )

    url = models.URLField(
        help_text="URL for the section"
    )

    body = HtmlField(
        help_text="Body of the article",
    )

    section = models.ForeignKey(
        "Section",
        help_text="Section containing this article",
    )


class Section(models.Model):
    title = models.TextField(
        help_text="Displayed as the heading for the recipe",
    )

    slug = models.SlugField(
        help_text="Used to set the URL - will be based on the title initially",
    )

    url = models.URLField(
        help_text="URL for the section"
    )

    parent = models.ForeignKey(
        "Section",
        blank=True,
        null=True,
        help_text="Parent section, if there is one",
    )

    def __str__(self):
        return self.slug
