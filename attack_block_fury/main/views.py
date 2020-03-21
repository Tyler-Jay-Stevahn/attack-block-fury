from django.shortcuts import render
from twilio.twiml.messaging_response import MessagingResponse

# Create your views here.


def landing_page(request):

    context = {

        "greeting": "heylo"

    }

    return render(request, 'landingpage.html', context)

def sms_reply(request):

    resp = MessagingResponse()

    resp.message('what it do?')

    response = str(resp)

    context = {

        "greeting": response
        }
    
    return render(request, 'smsreply.html', context)