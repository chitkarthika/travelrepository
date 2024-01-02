from django.urls import path, include

from . import views

urlpatterns = [
    # path('',views.display,name='display'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('testpage',views.test,name='test'),
    path('logout',views.logoutpg,name='logoutpg'),


    ]