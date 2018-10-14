# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'AC48ff4d9a4eafbef26a7077de52be9ca1'
auth_token = 'a3da1ef306d8d19b6a5394fe730c17ec'
client = Client(account_sid, auth_token)

def send(frequency, name):
    message = client.messages \
                    .create(
                        body="Pill Budy: It's time for you {} pills. Head on over to your Pill Budy \
                                and dispense your {}.".format(frequency, name),
                        from_='+17342928069',
                        to='+15863821255'
                    )

    print(message.sid)