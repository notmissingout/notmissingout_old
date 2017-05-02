from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render
from .models import Section, Article


def index(request):
    return render(request, 'navigation/index.html')


def victorian_health(request):
    return render(request, 'navigation/victorian_health.html')


def victorian_communication(request):
    return render(request, 'navigation/victorian_communication.html')


def victorian_entertainment(request):
    return render(request, 'navigation/victorian_entertainment.html')


def victorian_empire(request):
    return render(request, 'navigation/victorian_empire.html')


def victorian_childhood(request):
    return render(request, 'navigation/victorian_childhood.html')


def reflections(request):
    return render(request, 'navigation/reflections.html')


def navigation(request, path):
    def lookup_section(path):
        try:
            slug = path.split('/')[-1]
        except IndexError:
            return None

        candidates = Section.objects.filter(slug=slug)
        for candidate in candidates:
            print(candidate.url, path)
            if candidate.url == path:
                return candidate

        return None

    article_instance = None
    section_instance = lookup_section(path)
    print ("SI: {}".format(section_instance))
    if section_instance is None:
        section_instance = lookup_section(path.rsplit('/', 1)[0])
        if section_instance is None:
            raise Http404

        article_instance = Article.objects.get(
            section=section_instance,
            slug = path.rsplit('/', 1)[1]
        )
        if article_instance is None:
            raise Http404

    if section_instance is None:
        raise Http404

    if article_instance is None:
        return render(
            request, 'navigation/section.html', {
                "section": section_instance,
            }
        )
    else:
        return render(
            request, 'navigation/article.html', {
                "section": section_instance,
                "article": article_instance,
            }
        )
