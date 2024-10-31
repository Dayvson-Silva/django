
from django.contrib import admin
from django.urls import path
from .views import home , product , autenticar , pessoas

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home),
    path('product/', product),
    path('autenticar/', autenticar),
    path('pessoas/',pessoas)
]
