
from django.urls import path
from .views import get_tarefas


urlpatterns = [

path('', get_tarefas ,name = 'tarefas')

]