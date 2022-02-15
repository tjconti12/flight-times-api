from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('airports/', views.AirportList.as_view(), name='airport_list'),
    path('airports/<int:pk>', views.AirportDetail.as_view(), name="airport_detail")
]