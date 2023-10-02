from twilio.rest import Client

account_sid = 'ACa71a7a6ede9e710fb2733a632d57b160'
auth_token = '8274398bdd890f27fe024382822267cd'
client = Client(account_sid, auth_token)

def sendSms():
    message = client.messages.create(
    from_='+19287547597',
    body='Alert ! Human Intruder Detected ',
    to='+918446835357'
    )

    print(message.sid) 