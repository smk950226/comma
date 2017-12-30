from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^act/photo/$', views.act_photo, name='act_photo'),
    url(r'^act/photo/add$',views.act_photo_add, name='act_photo_add'),
]