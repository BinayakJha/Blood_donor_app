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

from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from core import views
from django.conf.urls.static import static
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
    path('blood_request_form_submit/', views.BloodRequests.form_function, name='blood_request_form_submit'),
    path('email_send/', views.BloodRequests.send_info_email, name='email_send'),
    # path('delete_blood_request/', views.BloodRequests.delete_request, name='delete_blood_request'),
    path('edit_extra/', views.Tabs.user_extra_contact, name='edit_extra'),
    path('edit_extra_submit/', views.User_Extra_Info.user_extra_info, name='edit_extra_submit'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [path('silk/', include('silk.urls', namespace='silk'))]