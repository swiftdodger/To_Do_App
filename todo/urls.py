from django.urls import path
from todo import views
from todo.views import task_update

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('add/', views.task_create, name='task_create'),
    path('<int:pk>/edit/', views.task_update, name = 'task_update'),
    path('<int:pk>/delete/', views.task_delete, name = 'task_delete'),

]
