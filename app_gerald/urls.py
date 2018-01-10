from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^list/$', views.PersonListView.as_view(), name='list'),
    url(r'^(?P<pk>[0-9]+)/$', views.PersonView.as_view(), name='person'),
    url(r'^women/$', views.GetWomanView.as_view(), name='get_woman'),
    url(r'^king/$', views.GetKing.as_view(), name='get_king'),
    url(r'^find/$', views.find, name='find'),
    url(r'^find_person/$', views.find_person, name='findperson'),
]
