
"""
URL configuration for djangoCRUD project.

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
from django.urls import path, include
from tasks import views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name='home'),

    path('sign-up/', views.sign_up, name='sign-up'),

    # path('notes/', include('notes.urls'), name='notes'),
    path('tasks/', views.tasks_view, name='tareas_view'),
    path('tasks/create/', views.task_create, name='task_create'),

    path('log-out/', views.salir, name='log-out'),

    path('log-in/', views.ingresar, name='ingresar'),

    path('tasks/<int:task_id>/', views.task_detail, name='task_detail'),

    path('tasks/<int:task_id>/delete/', views.task_deleted, name='task_deleted'),


    path('tasks/<int:task_id>/task-completed/', views.task_completed, name='task_completed'),
    path('tasks/all-tasks/', views.all_tasks, name='all_tasks'),

]
