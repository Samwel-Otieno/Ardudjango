from django.urls import path
from . import views
app_name='ardudjango'

urlpatterns=[
    path('index/', views.index, name='index'),
]