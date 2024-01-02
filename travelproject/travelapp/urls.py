from .import views
from django.urls import path

urlpatterns = [

    path('',views.display,name='display'),
    path('homepage/',views.homepg,name='homepage'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('details/',views.details,name='details'),
    path('thanks/',views.thanks,name='thanks'),
    path('contact/',views.contact,name='contact'),

]
