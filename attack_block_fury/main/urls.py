from django.urls import path
from .views import landing_page, sms_reply

urlpatterns = [
    path('sms/', sms_reply, name='sms_reply'),
    path('', landing_page, name='landing_page')
]
 