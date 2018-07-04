from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'index', views.site, name='site'),
    url(r'inserir', views.add_water, name='add_water'),
]
