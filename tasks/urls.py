from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.get_all, name='list'),
    path('create-task', views.add_task, name='create_task'),
    path('create-category', views.add_category, name='create_category'),
    path('update-task/<str:task_id>/', views.update_task, name="update_task"),
    path('delete-task/<str:task_id>/', views.delete_task, name="delete_task"),
    path('category/<str:cat_id>', views.get_category, name="get_category"),
    path('update-category/<str:cat_id>/', views.update_category, name="update_category"),
    path('delete-category/<str:cat_id>/', views.delete_category, name="delete_category"),
    path('completed', views.get_completed, name="get_completed"),
    path('mark-complete/<str:task_id>', views.mark_task_complete, name="mark_task_complete")
]
