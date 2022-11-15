from django.urls import path
from . import views

urlpatterns = [
    path('', views.course, name='index'),
    path('register/', views.register, name='register'),
    path('edit/<int:id_course>', views.edit, name='edit'),
    path('remove/<int:id_course>', views.remove, name='remove'),
    path('new_data/', views.new_data, name='new_data')
]
