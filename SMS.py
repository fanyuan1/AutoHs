from twilio.rest import Client 
 
def sendMessage(msg = 'Something went wrong with Auto HearthStone..'):
	sendEmail(msg)

# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def sendEmail(subject='Sending with Twilio SendGrid is Fun'):
	try:
		message = Mail(
		    from_email='',
		    to_emails='',
		    subject=subject,
		    html_content=subject)

		sg = SendGridAPIClient('')
		response = sg.send(message)
		# print('Success')
		# print(response.status_code)
		# print(response.body)
		# print(response.headers)
	except Exception as e:
		print('[error occured]')
		print(e.to_dict)

if __name__ == '__main__':
	# sendMessage()
	sendEmail('Subject')