from django.shortcuts import render
from .models import twilio
from django_twilio.decorators import twilio_view
from twilio.twiml.messaging_response import MessagingResponse
from .send_to_user import send_it

# Create your views here.


def landing_page(request):

    context = {

        "greeting": "heylo"

    }

    return render(request, 'landingpage.html', context)

@twilio_view
def sms_send(request):

    r = MessagingResponse()

    message = 'wow what to do now'

    r.message(message)

    return r

def sms_receive(request, receiver, sender, body):
    
    send_it(receiver, sender, body)
