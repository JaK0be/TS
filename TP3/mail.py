import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import sys
import os

def sendEmail(sendTo, code):
	email = 'tsfilesystem@gmail.com'
	password = 'ts@f1lesystem'
	send_to_email = sendTo
	subject = 'Security Code'
	message = str(code)


	msg = MIMEMultipart()
	msg['From'] = email
	msg['To'] = send_to_email
	msg['Subject'] = subject

	 # Attach the message to the MIMEMultipart object
	msg.attach(MIMEText(message, 'plain'))

	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(email, password)
	text = msg.as_string() # You now need to convert the MIMEMultipart object to a string to send
	server.sendmail(email, send_to_email, text)
	server.quit()

code = int.from_bytes(os.urandom(4), byteorder="little")
sendEmail("pedrotgoncalves@hotmail.com", code)