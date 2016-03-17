from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add$', views.add, name='add'),
    url(r'^edit/(?P<id>.*)$', views.edit, name='edit'),
    url(r'^delete/(?P<id>.*)$', views.delete, name='delete'),
    url(r'^item/add/(?P<ticket_id>.*)/(?P<id>.*)$', views.add_item, name='add_item'),
    url(r'^item/delete/(?P<id>.*)$', views.delete_item, name='delete_item'),
]