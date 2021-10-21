from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from dogs import views

app_name = 'dogs'

urlpatterns = [
    url(r'^dogs/$', views.DogList.as_view()),
    url(r'^dogs/(?P<pk>[0-9]+)/$', views.DogDetail.as_view()),
    url(r'^breeds/$', views.BreedList.as_view()),
    url(r'^breeds/(?P<pk>[0-9]+)/$', views.BreedDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)