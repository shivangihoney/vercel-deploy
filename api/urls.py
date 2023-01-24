from django.urls import path
from api import views

urlpatterns = [
    path( 'company/', views.comapnyList.as_view()),
]
