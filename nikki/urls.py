from django.urls import path
from .import views

app_name = 'nikki'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('add/', views.add, name='add'),
    path('upadate/<int:pk>/', views.update, name='update'),
    path('delete/<int:pk>', views.delete, name='delete'),
]
