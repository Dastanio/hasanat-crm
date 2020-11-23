from django.urls import path
from . import views

urlpatterns = [
	path('', views.main, name = 'main'),
	path('space/<int:space_id>/', views.SpaceDetail, name = 'space_detail_url'),
	path('task/<int:list_id>/', views.task, name = 'task_url'),
	# path('subtask/<int:task_id>/', views.subtask, name = 'subtask_url'),
	path('task_detail/<int:list_id>/<int:task_id>/', views.TaskDetail, name = 'task_detail_url'),
	path('status/<int:task_id>/', views.status, name = 'status_url'),
	#DRF
	path('task_create_api/', views.TaskCreateView.as_view(), name = 'TaskCreateView'),
	path('task_list_api/', views.TaskListView.as_view(), name = 'TaskListView'),
	path('task_detail_api/<int:pk>/', views.TaskDetailView.as_view(), name = 'TaskDetailView')
] 