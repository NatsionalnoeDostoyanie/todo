from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add, name='add'),
    path('update/<int:task_id>/', views.update, name='update'),
    path('delete/<int:task_id>/', views.delete, name='delete'),
    path('registration/', views.registration, name='registration'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='index'), name='logout'),
]