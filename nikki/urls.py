from django.urls import path
from .import views

app_name = 'nikki'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('add/', views.AddView.as_view(), name='add'),
    path('upadate/<int:pk>/', views.UpdateView.as_view(), name='update'),
    path('delete/<int:pk>', views.DeleteView.as_view(), name='delete'),
]
