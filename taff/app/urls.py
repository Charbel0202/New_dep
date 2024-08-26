from django.urls import path
from app import views

urlpatterns = [
    path('', views.index, name="index"),
    path('update', views.update, name="update"),
    path('insert', views.insertData, name="insertData"),
    path('delete/<Student_id>', views.delete, name="delete"),
    path('update/<Student_id>', views.update, name="update"),
]