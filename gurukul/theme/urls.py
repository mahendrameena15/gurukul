"""
URL configuration for gurukul project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include
from theme import views
from .theme_custom_views import admission
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('about-us',views.about_us,name='about-us'),
    path('contact-us',views.contact_us,name='contact-us'),
    path('admission-form',views.admission_form,name='admission-form'),
    path('gallery',views.gallery,name='gallery'),
    path('about-admission',views.about_admission,name='about-admission'),
    path('student-life',views.student_life,name='student-life'),
    path('calendar',views.calendar,name='calendar'),
    path('activities',views.about_activities,name='activities'),
    path('about-course',views.about_course,name='about-course'),
    path('donation',views.donation,name='donation'),
    path('class-routine',views.class_routine,name='class-routine'),
    path('thankyou',views.thankyou,name='thankyou'),
    path('success',views.success,name='success'),
    path('404-Error',views.error_page,name='404-Error'),
    path('contact_us_view',views.contact_us_view,name='contact_us_view'),
    path('home-touch',views.home_get_in_touch,name='home-touch'),
    path('admission-touch',views.admission_get_in_touch,name='admission-touch'),
    path('about-touch',views.about_get_in_touch,name='about-touch'),
    #POST Admission
    path("admission-form-view",admission.admission_form_view,name="admission-form-view"),    

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
