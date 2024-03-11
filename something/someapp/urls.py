
from django.urls import path
from someapp import views
urlpatterns = [
    path('', views.create, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('edit/<sid>', views.edit, name='edit'),
    path('delete/<did>', views.delete, name='edit'),
]
