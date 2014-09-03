from django.conf.urls import patterns, url
from django_mnemonic.views import SimpleAPIView, CamelAPIView

urlpatterns = patterns('',
    url(r'^api/(?P<count>[0-9]+)/?$', SimpleAPIView.as_view()),
    url(r'^api/camel/(?P<count>[0-9]+)/?$', CamelAPIView.as_view()),
)
