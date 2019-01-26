from django.conf.urls import url
from . import views
from django.views.generic.base import RedirectView, TemplateView
from django.contrib import admin
from django.urls import path, include

app_name = 'mainApp'

urlpatterns = [
    url(r'^$', views.signup_view, name='signup'),
    url(r'login*$',views.login_view,name ='login'),
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/favicon/favicon.ico')),
    # path('template/login.html', TemplateView.as_view(template_name='login.html'), name='login'),
    # path('admin/', admin.site.urls),
    # path('accounts/', include('django.contrib.auth.urls'))
]