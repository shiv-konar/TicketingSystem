"""TicketingSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import RedirectView
import home.views
import contact.views
import logissue.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^register/', include('Register.views.register'), name='register'),
    url(r'^accounts/', include('registration.backends.default.urls'), name='accounts'),
    url(r'^$', RedirectView.as_view(url='/accounts/login')),
    url(r'^contact/', contact.views.contact , name='contact'),
    #url(r'^logissue/', logissue.views.logissue, name='logissue'),
    url(r'^accounts/profile', logissue.views.logissue, name='logissue'),
]