from django.urls import path
from .views import landing_page, sms_send

urlpatterns = [
    path('sms/', sms_send, name='sms_send'),
    path('', landing_page, name='landing_page')
]
 