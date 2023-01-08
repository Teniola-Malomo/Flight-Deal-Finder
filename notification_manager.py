from twilio.rest import Client
from users_data_manager import UsersDataManager
import smtplib

TWILIO_SID = "AC398bdd275fb8f66e4a001cea4b4a0554"
TWILIO_AUTH_TOKEN = "a973a1f9301f31a6ac393ca99f59e657"
TWILIO_VIRTUAL_NUMBER = "+12672973841"
TWILIO_VERIFIED_NUMBER = "+353899418172"

class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)


    def send_emails(self, message, link=None):
        port = 465
        my_email = "chopchip623@gmail.com"
        my_password = "ceqghnhxxxkcgeeb"
        users_data_manger = UsersDataManager()
        receiver_emails = users_data_manger.get_users_emails()

        server = smtplib.SMTP_SSL("smtp.gmail.com", port)
        server.login(my_email, my_password)
        message = message.encode('utf-8')
        for email in receiver_emails:
          server.sendmail(my_email, [email], message)

# nm = NotificationManager()
# nm.send_emails("Hello")