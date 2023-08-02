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
from django.urls import path
from admin_panel import views
from .custom_views import frontend, dashboard,users,courses,categories
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', frontend.login, name='login'),
    path('admin-login', frontend.admin_login, name='admin-login'),
    path('dashboard', dashboard.dashboard, name='dashboard'),
    #Users
    path('add-user', users.add_user, name='add-user'),
    path('edit-user', users.edit_user, name='edit-user'),
    path('users-list', users.user_list, name='users-list'),
    
    # path('all-users',users.user_list_view,name='all-users'),

    #Categories
    path('add-category', categories.add_category, name='add-category'),
    path('edit-category',categories.edit_category, name='edit-category'),
    path('category-list',categories.category_list, name='category-list'),
    #Courses
    path('add-course', courses.add_course, name='add-course'),
    path('edit-course',courses.edit_course, name='edit-course'),
    path('course-list',courses.course_list, name='course-list'),

    path('success',views.success, name='success'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
