from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import logout_view,RegisterView,add_employee
from empapp.views import home,index


urlpatterns = [
    path('login/',auth_views.LoginView.as_view(template_name='accounts/login.html'),name='login'),
    path('logout/',logout_view,name='logout'),
    path('register/',RegisterView.as_view(),name='register'),
    path('accounts/profile/',home,name='home'),
    path('add/',add_employee,name='add_employee'),
    path('',index,name="index.html"),
]