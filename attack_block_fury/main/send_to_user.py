from twilio.rest import Client
from .models import twilio

# Your Account SID from twilio.com/console
# Your Auth Token from twilio.com/console

receiver = "+15806301485"
sender = "+12016854951"
body = "yo this is your boi tyler"


def send_it(receiver, sender, body):
    client = Client(twilio.objects.get(id=1))
    
    message = client.messages.create(to=receiver, from=sender, body=body)