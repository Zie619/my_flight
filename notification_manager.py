from twilio.rest import Client
import smtplib

TWILIO_SID = 'AC1c61134e464b34857a6b93ca61f07877'
TWILIO_AUTH_TOKEN = '963a7364f9ab6f8a88d61b0c78f88d2d'
TWILIO_MSG_SERVICE = 'MG93ea846be13af04244027beb7240e7de'
TWILIO_ALPHA_SENDER = 'AIe679781f7b9ff40242116c9dec64a97f'
TWILIO_VERIFIED_NUMBER = '+919892827387'
MAIL_PROVIDER_SMTP_ADDRESS = 'smtp.gmail.com'
MY_EMAIL = 'xeliadx@gmail.com'
MY_PASSWORD = 'kxlvhkzxntkvihnl'


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def SendSms(self, message, link):
        message = self.client.messages.create(
            messaging_service_sid=TWILIO_MSG_SERVICE,
            media_url=[link],
            body='New Low Price Flight to :' + message,
            to='+972536622456'
        )
        print(message.sid)


    def SendMails(self, emails, message, google_flight_link):
        with smtplib.SMTP(host=MAIL_PROVIDER_SMTP_ADDRESS, port=587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight to {message} !\n\n\n{google_flight_link}".encode('utf-8')
                )


# hello = NotificationManager()
# # emails = ['xeliadx@gmail.com']
# # hello.SendMails(emails , 'country' , 'https://demo.twilio.com/owl.png')
# hello.SendSms('istan' , 'https://demo.twilio.com/owl.png')