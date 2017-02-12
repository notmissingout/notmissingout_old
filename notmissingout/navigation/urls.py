from django.conf.urls import url

from . import views

app_name = 'navigation'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(
        r'^little_learners/victorians/health$',
        views.victorian_health,
        name='victorian_health'
    ),
    url(
        r'^little_learners/victorians/communication$',
        views.victorian_communication,
        name='victorian_communication'
    ),
    url(
        r'^little_learners/victorians/entertainment$',
        views.victorian_entertainment,
        name='victorian_entertainment'
    ),
    url(
        r'^little_learners/victorians/empire$',
        views.victorian_empire,
        name='victorian_empire'
    ),
    url(
        r'^little_learners/victorians/childhood$',
        views.victorian_childhood,
        name='victorian_childhood'
    ),
    url(r'^reflections$', views.reflections, name='reflections'),
    url(r'^(?P<path>.*)/?$', views.navigation, name='navigation'),
]
