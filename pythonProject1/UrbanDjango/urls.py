from django.contrib import admin
from django.urls import path, include

urlpatterns = [
       path('admin/', admin.site.urls),
       path('task3/', include('task3.urls')),  # Включаем маршруты вашего приложения
   ]