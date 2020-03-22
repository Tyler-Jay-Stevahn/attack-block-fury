from django.db import models

# Create your models here.
class twilio(models.Model):
    twilio_account_sid = models.CharField(max_length=40)
    twilio_auth_token = models.CharField(max_length=40)