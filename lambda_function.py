import base64
import json
import os
from twilio.rest import Client
from urllib.parse import urlencode

TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")



def lambda_handler(event, context):
    to = event['To']
    from_=event['From']
    inputmessage=event['message']
    twiml = {
        'Twiml': '<Response>\n' +
                 '<Say voice="alice">'+str(inputmessage)+'</Say>\n' +
                 '</Response>'
    };
    url = "http://twimlets.com/echo?" + urlencode(twiml);

   
    print(url,to)
    try:
        # perform HTTP POST request
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        call = client.calls.create(
            to=to,
            from_=from_,
            url=url)
        print(call.sid)

    except Exception as e:
        # something went wrong!
        return e

    return 'called successfully'

#event={"To":"+XXXXXXXXXXXX","From":"+XXXXXXXXXX","message":"hi how are you?"}
#context=None
#lambda_handler(event,context)
