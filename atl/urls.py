from django.urls import path
from . import views
app_name = 'atl'
urlpatterns = [
    path('', views.task_list, name = 'index'),
    #path('<int:task_id>/', views.detail, name='detail'),
]
