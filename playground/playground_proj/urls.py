from django.contrib import admin
from django.urls import path
from playground_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('playgroundApp/', views.index),
]
