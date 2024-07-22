from django.urls import path
from . import views


urlpatterns = [
   path('', views.home, name="home"),
   path('qmo_member/', views.qmo_member, name="qmo_member"),
   path('join/', views.join, name="join"),
]
