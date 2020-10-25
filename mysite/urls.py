from django.contrib import admin
from django.urls import path, include
from mywed import views
from django.contrib.auth import views as aunt_views

urlpatterns = [
    path('', aunt_views.LoginView.as_view(template_name='mywed/login.html'), name='login'),
	path('index', views.index , name='index'),
	path('signup', views.signup, name='signup'),
    path('logout',views.logout, name='logout'),
    path('foradmin',views.foradmin, name='foradmin'),
    path('contact',views.contact, name='contact'),
#	path('mywed/', include('mywed.urls')),
	path('admin/', admin.site.urls),
]
