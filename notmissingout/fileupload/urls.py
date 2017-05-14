from django.conf.urls import url

from . import views

app_name = 'fileupload'
urlpatterns = [
    url(r'^image$', views.upload_attachment, name='upload_attachment'),
]
