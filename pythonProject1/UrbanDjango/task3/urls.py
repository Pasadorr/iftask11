from django.urls import path
from . import views

urlpatterns = [
       path('platform/', views.platform, name='platform'),
       path('games/', views.games, name='games'),
       path('cart/', views.cart, name='cart'),
   ]