from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render


def index(request):
    return render(request, 'navigation/index.html')


def victorian_health(request):
    return render(request, 'navigation/victorian_health.html')


def victorian_communication(request):
    return render(request, 'navigation/victorian_communication.html')


def reflections(request):
    return render(request, 'navigation/reflections.html')


def navigation(request, path):
    path = path.rstrip('/')

    def lookup_section(path):
        try:
            slug = path.split('/')[-2]  # slug of the instance
        except IndexError:
            return None

        candidates = Section.objects.filter(slug=slug)
        for candidate in candidates:
            if candidate.get_path() == path:
                return candidate
        return None

    article_instance = None
    section_instance = lookup_section(path)
    if section_instance is None:
        section_instance = lookup_section(path.rsplit('/', 1)[0])
        if section_instance is not None:
            article_instance = Article.objects.get(
                section=section_instance,
                slug = path.rsplit('/', 1)[1]
            )
            if article_instance is None:
                raise Http404

    if section_instance is None:
        raise Http404

    return render(
        request, 'navigation/article.html', (path, instance, article)
    )
