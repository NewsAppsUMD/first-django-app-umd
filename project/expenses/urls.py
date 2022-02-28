from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('summary/<int:summary_id>/', views.summary, name='summary'),
]
