from django.urls import path

from .views import *

urlpatterns = [
    path('tasklist/', Task_List_view.as_view(), name='task_list'),
    path('taskdetail/<int:pk>/', Task_detail_view.as_view(), name='task_detail'),
    path('categorylist/', category_list.as_view(), name='category_list'),
    path('categoryeach/', each_category, name='each_category'),
    path('eachlist/', each_list, name='each_list'),
    path('', home, name='home'),
    path('download/', json_file, name='Download'),
]
