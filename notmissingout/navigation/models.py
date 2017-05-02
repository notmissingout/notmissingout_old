from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from common import HtmlField


class Article(models.Model):
    title = models.TextField(
        help_text="Displayed as the title for the article",
    )

    slug = models.SlugField(
        help_text="Used to set the URL - will be based on the title initially",
    )

    body = HtmlField(help_text="Body of the article", )

    section = models.ForeignKey(
        "Section",
        help_text="Section containing this article",
    )

    def __str__(self):
        return self.url

    class Meta:
        unique_together = (("slug", "section"), )

    @property
    def url(self):
        return '/'.join((self.section.url, self.slug))


class Section(MPTTModel):
    title = models.TextField(
        help_text="Displayed as the heading for the recipe",
    )

    slug = models.SlugField(
        help_text="Used to set the URL - will be based on the title initially",
    )

    parent = TreeForeignKey(
        "self",
        null=True,
        blank=True,
        help_text="Parent section, if there is one",
    )

    @property
    def articles(self):
        return self.article_set.all().order_by("title")

    def __str__(self):
        return self.title

    class Meta:
        unique_together = (("slug", "parent"), )

    @property
    def url(self):
        ancestor_slugs = [
            section.slug
            for section in self.get_ancestors(include_self=True)
        ]
        if len(ancestor_slugs) == 0:
            return ''
        return '/'.join(ancestor_slugs)
