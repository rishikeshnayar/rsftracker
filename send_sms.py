# Using Twilio API to send SMS messages to my phone
from twilio.rest import Client
import twilio_creds

# Creates Twilio Client using my Twilio Account SID and Token credentials
client = Client(twilio_creds.account_sid, twilio_creds.token)

# Creates message and sends it
def text(body):
    message = client.messages \
                .create(
                     body = body,
                     from_='+18776296994',
                     to='+17328741798'
                 )
