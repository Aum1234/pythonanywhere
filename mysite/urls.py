from django.contrib import admin
from django.urls import path, include
from mywed import views

urlpatterns = [
	path('', views.index),
	path('mywed/', include('mywed.urls')),
	path('polls/', include('polls.urls')),
	path('admin/', admin.site.urls),
]
