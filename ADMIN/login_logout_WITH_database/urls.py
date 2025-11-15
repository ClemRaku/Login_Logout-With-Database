from django.urls import path
from . import views
urlpatters = [
    path('', views.index, name = 'index'),
    path('result/', views.result_page, name = 'result')
]