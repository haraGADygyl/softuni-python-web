from django.urls import path

from softuni_python_web_basics.tasks.views import home

urlpatterns = (
    path('', home),
)
