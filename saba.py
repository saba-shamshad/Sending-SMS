import os

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

from twilio.rest import Client
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body='''Hello Satya Sir!
                        This is Sample message for API Testing''',
         from_ =  +13342342930,
         to = +917992160083
     )

print(message.sid)

