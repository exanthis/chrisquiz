from django.urls import path, include
from .views import IgnoreQuestion

app_name="api"
urlpatterns = [
    path('ignore/<int:pk>', IgnoreQuestion.as_view(), name="ignore"),
]