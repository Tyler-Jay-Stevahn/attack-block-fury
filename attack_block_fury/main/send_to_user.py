from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC896924fffcc3cf4e45c108b11857708e"
# Your Auth Token from twilio.com/console
auth_token  = "83f446b27e37494f06f71dfbb10799e8"

receiver = "+15806301485"
sender = "+12016854951"
body = "yo this is your boi tyler"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to=receiver, 
    from_=sender,
    body=body)
