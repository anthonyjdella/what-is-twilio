import os

from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

def send_text():
	account_sid = os.getenv('TWILIO_ACCOUNT_SID')
	auth_token = os.getenv('TWILIO_AUTH_TOKEN')
	client = Client(account_sid, auth_token)

	message = client.messages.create(
		body="This is all the code you need to send a text with Twilio",
		from_='+19403948137',
		to='+14693470960'
	)
	print(message.body)

send_text()