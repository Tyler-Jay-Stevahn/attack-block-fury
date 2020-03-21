from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from twilio.twiml.messaging_response import MessagingResponse

# Create your views here.


def landing_page(request):

    context = {

        "greeting": "heylo"

    }

    return render(request, 'landingpage.html', context)

@csrf_exempt
def sms_reply(request):
    r = MessagingResponse()
    r.message('Hello from your Django app!')
    return HttpResponse(r.toxml(), content_type='text/xml')