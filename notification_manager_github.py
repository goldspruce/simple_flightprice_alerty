from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

YOUR_ACCOUNT_SID="ACb03834b942ea3d75ad7e6cf0cd6a9a87"
AUTH_TOKEN="redacted"
account_sid = YOUR_ACCOUNT_SID
auth_token = AUTH_TOKEN

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    
    def send_sms(self,message):
    	client = Client(account_sid, auth_token)
    	message = client.messages.create(
	 	body=message,
	 		from_="+18052108603",
         	to="+15104272049"
         	)
    	#print(message)
    	print(message.status)