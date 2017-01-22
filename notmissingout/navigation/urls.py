from django.conf.urls import url

from . import views

app_name = 'navigation'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^little_learners/victorians/health$', views.victorian_health, name='victorian_health'),
    url(r'^little_learners/victorians/communication$', views.victorian_communication, name='victorian_communication'),
    url(r'^reflections$', views.reflections, name='reflections'),
]
