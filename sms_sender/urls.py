from . import views
from django.urls import path

urlpatterns = [
    path('', views.sms_form, name='sms_form'),
    path('send', views.send_sms, name='send_sms')
    ]

