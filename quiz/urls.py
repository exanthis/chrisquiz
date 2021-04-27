from django.urls import path, include

from .views import index


app_name="quiz"
urlpatterns = [
    path('', index, name="index")
]