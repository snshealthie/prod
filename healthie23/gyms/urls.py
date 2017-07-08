from django.conf.urls import url
from gyms import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    # url(r'^/$', views),
    url(r'^/(?P<pk>[0-9]+)/$', views.GymDetail.as_view()),
    # url(r'^/', views.)
    url(r'^$', views.GymList.as_view())

]