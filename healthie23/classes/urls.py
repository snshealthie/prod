from django.conf.urls import url
from classes import views as v1
from reviews import views as v2
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [

    # url(r'^$', v1.ListCreateClasses.as_view(), name='classes_list'),
    # url(r'(?P<pk>\d+)/$', v1.RetreiveUpdateDestroyClasses.as_view(), name='classes_detail'),
    # url(r'^(?P<classes_pk>\d+)/reviews/(?P<pk>\d+)/$', v2.RetreiveUpdateDestroyReview.as_view(), name='review_detail'),
    # url(r'^(?P<classes_pk>\d+)/reviews/$', v2.ListCreateReview.as_view(), name='review_list'),
]
# urlpatterns = format_suffix_patterns(urlpatterns)
