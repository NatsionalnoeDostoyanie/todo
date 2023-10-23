from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add, name='add'),
    path('update/<int:task_id>/', views.update, name='update'),
    path('delete/<int:task_id>/', views.delete, name='delete'),
    path('registration/', views.registration, name='registration'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]