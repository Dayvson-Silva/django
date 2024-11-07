
from django.contrib import admin
from django.urls import path
from .views import  categorias,produtos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('categorias/', categorias,  name='categorias'),
    path('produtos/', produtos,  name='produtos')
]
