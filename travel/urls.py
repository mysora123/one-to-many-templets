from django.urls import path
from travel.views import *
app_name='travel'


urlpatterns=[
    path('index/',index,name='index'),
    path('registration/',registration,name='registration'),
    path('login/'.login,name='login'),
    path('home/',home,name='home'),

]