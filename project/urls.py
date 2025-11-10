from django.urls import path
from app.views import CalculatorView

urlpatterns = [
    path('calculate/', CalculatorView.as_view(), name='calculate'),
]
