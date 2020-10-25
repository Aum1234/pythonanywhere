from django.urls import path
from django.contrib.auth import views as aunt_views
from . import views

urlpatterns = [
    path('', aunt_views.LoginView.as_view(template_name='mywed/login.html'), name='login'),
    path('index', views.index, name='index'),
    path('signup', views.signup, name='signup'),
    path('contact', views.contact, name='contact'),
    path('foradmin', views.foradmin, name='foradmin'),
    path('logout',views.logout, name='logout'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]