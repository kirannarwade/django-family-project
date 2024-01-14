from django.urls import path
from home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('save-data/', views.save_data, name='save-data')
]