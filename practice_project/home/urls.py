from django.urls import path

from . import views
app_name = 'home' ##namespace url names
urlpatterns = [ 
    path('', views.home, name='home'), 
]