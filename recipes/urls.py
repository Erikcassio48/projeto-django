from django.http import HttpResponse
from recipes.views import home, contato, sobre
from django.urls import path



urlpatterns = [
    path('', home),

]
