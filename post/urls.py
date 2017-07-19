from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='gowno'),
    url(r'^create/$', views.post_create, name='gowno1'),
    url(r'^detail/$', views.post_detail, name='gowno2'),
    url(r'^update/$', views.post_update, name='gowno3'),
    url(r'^delete/$', views.post_delete, name='gowno4'),

]
