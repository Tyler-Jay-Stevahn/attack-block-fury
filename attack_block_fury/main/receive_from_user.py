from twilio.twiml.messaging_response import MessagingResponse
from flask import request, Flask, redirect

app = Flask (__name__)

@app.route('/sms', methods=['GET', 'POST'])
def sms_reply():
    resp = MessagingResponse()

    resp.message('what it do?')

    return str(resp)
