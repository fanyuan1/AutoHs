from twilio.rest import Client 
 
def sendMessage(msg = 'Something went wrong with Auto HearthStone..'):
	sendEmail(msg)

def sendSMS(msg = 'Something went wrong with Auto HearthStone..'):
	account_sid = 'AC41b9707d4e78aa3b2585bb8bedf2410e' 
	auth_token = '34f0e5fbb91ecb91ea4a0b4576a50288' 

	client = Client(account_sid, auth_token) 

	
	 
	message = client.messages.create(  
	                              messaging_service_sid='MG2fe10e9322609b77b3d74a77fc2cfc11', 
	                              body=msg,      
	                              to='+12016885430' 
	                          ) 
	 
	# print(message.sid)


# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def sendEmail(subject='Sending with Twilio SendGrid is Fun'):
	try:
		message = Mail(
		    from_email='lifeiteng@163.com',
		    to_emails='li.feiteng@gmail.com',
		    subject=subject,
		    html_content=subject)

		sg = SendGridAPIClient('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')
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