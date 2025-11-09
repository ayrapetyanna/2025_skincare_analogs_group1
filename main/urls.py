from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('analogs/', views.analogs, name='analogs'),
    path('find/', views.find_analog, name='find_analog'),
    path('login/', views.login_view, name='login'),
    path('favorites/', views.favorites, name='favorites'),
]
