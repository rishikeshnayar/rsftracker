# Using Twilio API to send SMS messages to my phone
from twilio.rest import Client

# Creates Twilio Client using my Twilio Account SID and Token credentials
client = Client('AC1437ac9f993248bf1ff084256aa4c1b5', 'ea11c801f73baede7365f0ffac58ac82')

# Creates message and sends it
def text(body):
    message = client.messages \
                .create(
                     body = body,
                     from_='+18776296994',
                     to='+17328741798'
                 )
