from django.conf.urls import url
from . import views
from django.views.generic.base import RedirectView


urlpatterns = [
    url(r'^$', views.signup, name='signup'),
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/favicon/favicon.ico'))
]