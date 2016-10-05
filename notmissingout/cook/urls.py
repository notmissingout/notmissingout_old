from django.conf.urls import url

from . import views

app_name = 'cook'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'(?P<slug>[^/]+)$', views.recipe, name='recipe'),
]
