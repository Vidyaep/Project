from django.urls import path
from studentapp.views import *

urlpatterns = [
    path('hello', hello_world, name='hello_world'),
    path('list',student_list,name='student-list'),
    # path('add',student_add,name='student-add'),
    # path('<int:student_id>/delete',student_delete,name='student-delete'),
    path('<int:student_id>/edit',student_edit,name='student-edit'),
    # path('<int:student_id>/update',student_update,name='student-update')
]