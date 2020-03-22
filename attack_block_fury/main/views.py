from django.shortcuts import render
from django_twilio.decorators import twilio_view
from twilio.twiml.messaging_response import MessagingResponse

# Create your views here.


def landing_page(request):

    context = {

        "greeting": "heylo"

    }

    return render(request, 'landingpage.html', context)

@twilio_view
def sms_reply(request):

    r = MessagingResponse()

    message = 'wow what to do now'

    r.message(message)

    return r