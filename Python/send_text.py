from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACc56a46f20f6f4b2a0cf65323c8145922"
# Your Auth Token from twilio.com/console
auth_token  = "37f5ae8179fbcb3f67125690faa0e598"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+14693484233", 
    from_="+19725219072",
    body="Hello from Python!")

print(message.sid)
