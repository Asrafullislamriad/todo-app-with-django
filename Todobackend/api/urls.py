 
from django.urls import path
from api import views

urlpatterns = [
    path('api/', views.BlogList.as_view()),
    path('details/<int:pk>', views.ApiDetail.as_view()),
]
