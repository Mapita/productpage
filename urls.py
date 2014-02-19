from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns as patterns
from django.views.generic import TemplateView

urlpatterns = patterns('',
    (r'^$', TemplateView.as_view(template_name="index.html")),
    (r'^what-makes-it-different/$', TemplateView.as_view(template_name="what-makes-it-different.html")),
    (r'^products-and-services/$', TemplateView.as_view(template_name="products-and-services.html")),
    (r'^our-customers/$', TemplateView.as_view(template_name="our-customers.html")),
    (r'^about-us/$', TemplateView.as_view(template_name="about-us.html")),
)
