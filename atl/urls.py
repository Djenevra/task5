from django.urls import path
from . import views
app_name = 'atl'
urlpatterns = [
    path('sort/', views.index, name='index'),
    path('sort/<int:task_id>/take/', views.take_task, name='take_task')



]
