from django.conf.urls import url
from . import views
from django.views.generic.base import RedirectView, TemplateView
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    url(r'^$', views.signup, name='signup'),
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/favicon/favicon.ico')),
    path('template/login.html', TemplateView.as_view(template_name='home.html'), name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls'))
]