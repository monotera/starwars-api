from django.urls import path
from . import views

# URLconf
urlpatterns = [
    path('', views.hello_world)
]
