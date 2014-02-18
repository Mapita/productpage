from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

urlpatterns = patterns('',
    (r'^', TemplateView.as_view(template_name="index.html")),
    (r'^what-makes-it-different/', TemplateView.as_view(template_name="what-makes-it-different.html")),
    (r'^why-maps/', TemplateView.as_view(template_name="why-maps.html")),
    (r'^our-customers/', TemplateView.as_view(template_name="our-customers.html")),
    (r'^about-us/', TemplateView.as_view(template_name="about-us.html")),
)
