from django.conf.urls import url
from django.urls import path
from passport_organization import views
app_name = 'passport_organization'
urlpatterns=[
    path('', views.passport_index, name="passport_index"),
    path('match-fingerprint/', views.finger_print, name="passport_finger_print"),
]