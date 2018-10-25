from django.urls import path
from . import views
app_name = 'atl'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:task_id>/', views.detail, name='detail'),
]
