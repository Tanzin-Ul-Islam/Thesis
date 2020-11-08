from django.conf.urls import url
from django.urls import path
from passport_organization import views
app_name = 'passport_organization'
urlpatterns=[
    path('', views.index, name="index"),
    path('/finger_print', views.finger_print, name="finger_print"),
    path('/apply', views.apply_passport, name="apply_passport"),
]