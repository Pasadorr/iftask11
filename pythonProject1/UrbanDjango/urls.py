from django.contrib import admin
from django.urls import path, include

urlpatterns = [
       path('admin/', admin.site.urls),
       path('task2/', include('task2.urls')),  # Подключение маршрутов приложения task2
   ]