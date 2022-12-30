from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cardiovascular.urls')),
    #path('', include('MLapp.urls'))
]
