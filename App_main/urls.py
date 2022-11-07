from django.urls import path
from . import views


app_name = 'App_main'

urlpatterns = [
    path('', views.index, name='index'),
    path('member-dashboard', views.member_dashboard, name='member-dashboard'),
    path('admin-dashboard', views.admin_dashboard, name='admin-dashboard'),
    path('assign-trainers', views.assign_trainers, name='assign-trainers'),
    path('total-members', views.total_members, name='total-members'),
    path('health-check', views.health_check, name='health-check'),
    path('diet-chart', views.diet_chart, name='diet-chart'),

]
