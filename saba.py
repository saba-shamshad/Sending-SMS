import os

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

from twilio.rest import Client
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body='''Hello Satya Sir!
                        This is Sample message for API Testing''',
         from_ =  From_NUMBER,
         to = To_Number
     )

print(message.sid)

