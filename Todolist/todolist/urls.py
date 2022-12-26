from django.urls import path
from . import views
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate,TaskDelete,TaskLogin, TaskRegister
from django.contrib.auth.views import LogoutView

urlpatterns = [ 
    # path('', views.home, name='home'),
    path ('logout/', LogoutView.as_view(next_page = 'task-login'), name='task-logout'),
    path ('login/', TaskLogin.as_view(), name='task-login'),
    path ('register/', TaskRegister.as_view(), name='task-register'),
    path ('', TaskList.as_view(), name='tasks'),
    path ('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path ('task-create/', TaskCreate.as_view(), name='task-create'),
    path ('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path ('task-delete/<int:pk>', TaskDelete.as_view(), name='task-delete'),
]