from django.conf.urls import url
from . import views
from django.views.generic import (TemplateView, 
    RedirectView,
)
urlpatterns = [
	url(r'^$', views.landing_page, name="landing_page"),
    url(r'^home_page/$', views.home_page, name="home_page"),
	url(r'^home_page/(?P<year>[0-9]+)$', views.home_page, name="home_page"),
	]