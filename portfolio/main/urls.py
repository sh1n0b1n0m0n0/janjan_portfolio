from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('kill-cicero', views.kill_cicero),
    path('ave-cicero', views.ave_cicero)
]