from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # You will use this for the independent login page
    # path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
]