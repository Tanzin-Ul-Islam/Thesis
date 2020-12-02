from django.conf.urls import url
from django.urls import path
from central_organization import views
app_name = 'central_organization'
urlpatterns=[
    path('', views.index, name="index"),
    path('finger_print/', views.finger_print_process, name="finger_print"),
]