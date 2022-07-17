"""blood_donor_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from core import views
urlpatterns = [
    path('admin/', admin.site.urls),
    # add the views from core app
    path('', views.Tabs.index, name='index'),
    path('blood_requests/', views.Tabs.blood_requests, name='blood_requests'),
    path('profile/', views.Tabs.profile, name='profile'),
    path('login/', views.Tabs.login, name='login'),
    path('login_success/', views.Authentication.login, name='login_success'),
    path('register/', views.Tabs.register, name='register'),
    path('signup_success/', views.Authentication.signup, name='signup_success'),
    path('logout/', views.Authentication.logout, name='logout'),
    path('blood_request_form/', views.Tabs.blood_request_form, name='blood_request_form'),
    
    
]
