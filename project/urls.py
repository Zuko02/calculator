from django.urls import path
from app.views import FrontendAppView
from django.urls import path, include, re_path

urlpatterns = [
    path('calculate/', include('app.urls')),  # your calculator API
    re_path(r'^.*$', FrontendAppView.as_view(), name='frontend'),  # React routes
]

