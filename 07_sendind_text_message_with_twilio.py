#from twilio.rest import Client         # one way
from twilio import rest                 # other way


# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'AC4a59c7f571c53e72b35f9341844c9158'
auth_token = 'bd58f001ebbdfe74aa453ef34b9577c4'

#client = Client(account_sid, auth_token)    # one way
client = rest.Client(account_sid, auth_token)  # other way


# Note: this will not work if your number is in do not call registry
message = client.messages.create(
                     body="testing twilio with python. ",
                     from_="+14092457807",
                     to="+919891450298"
                 )

print(message.sid)
