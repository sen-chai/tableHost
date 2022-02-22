from django.urls import path
from .views import TestView, ViewPedidos

urlpatterns = [
    path('pedidos',ViewPedidos.as_view()),
    path('test',TestView.as_view()),
]