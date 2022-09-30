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
from django.urls import path, include
from django.contrib.auth import views as auth_views
from English import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
                  path("admin/", admin.site.urls),
                  path("", views.index, name="index"),
                  path("index.html", views.index, name="index"),
                  path("signup.html", views.register_request, name="register"),
                  path("login.html", views.login_request, name="login"),
                  path("logout.html", views.logout_request, name="logout"),
                  path("quiz.html", views.quiz, name="quiz"),
                  path("start.html", views.start, name="start"),
                  path("homeworks.html", views.homeworks, name="homeworks"),
                  path("contact.html", views.contact, name="contact"),
                  path('accounts/', include('django.contrib.auth.urls')),
                  path('password_reset_done.html',
                       auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
                       name='password_reset_done'),
                  path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
                      template_name="password_reset_confirm.html"), name='password_reset_confirm'),
                  path('password_reset_complete.html', auth_views.PasswordResetCompleteView.as_view(
                      template_name='password_reset_complete.html'), name='password_reset_complete'),
                  path("password_reset.html", views.password_reset, name="password_reset"),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

