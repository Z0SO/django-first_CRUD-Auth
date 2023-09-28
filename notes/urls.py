from django.urls import path
from . import views

urlpatterns = [
    path('loba/', views.note_loba, name='loba'),
]
