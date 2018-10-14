from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('learn', views.learn, name='learn'),
    path('register/', views.register, name='register'),
    path('register_success/', views.register_success, name='register_success'),
    path('login/', views.login, name='login'),
    path('setup/', views.setup,name='setup'),
    path('schedule/', views.schedule,name='schedule'),
    path('schedule/list', views.ScheduleListView.as_view(), name='schedule_list'),
    path('schedule/<int:pk>/delete/', views.ScheduleDelete.as_view(), name='schedule_delete')
]