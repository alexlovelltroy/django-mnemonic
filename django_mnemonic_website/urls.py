from django.conf.urls import patterns, url
from django_mnemonic.views import WordsFormView

urlpatterns = patterns('',
    url(r'^$', WordsFormView.as_view(template_name="base.html")),
    url(r'^(?P<count>[0-9]+)/?$', WordsFormView.as_view(template_name="base.html")),
    url(r'^camel/(?P<count>[0-9]+)/?$', WordsFormView.as_view(template_name="base.html"), {'camelcase': True,}),
)
