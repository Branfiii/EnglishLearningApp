"""EnglishLearning URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.template.defaulttags import url
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.views.static import serve

from English import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path("index.html", views.index, name="index"),
    path("signup.html", views.register_request, name="register"),
    path("login.html", views.login_request, name="login"),
    path("logout.html", views.logout_request, name= "logout"),
    path("quiz.html",views.quiz,name="quiz"),
    path("start.html",views.start,name="start"),
    path("homeworks.html",views.homeworks,name="homeworks"),
    path("contact.html",views.contact,name="contact"),
    path('accounts/', include('django.contrib.auth.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

