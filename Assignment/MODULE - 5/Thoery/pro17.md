##### Sending emails and OTPs using third-party APIs like Twilio, SendGrid.
###### Twilio (SMS OTP):

- Install: pip install twilio

Use Client to send SMS with a generated OTP.
```python
Example:

from twilio.rest import Client
import random

def send_otp_sms(phone):
    otp = str(random.randint(1000, 9999))
    Client("SID", "TOKEN").messages.create(
        body=f"Your OTP is {otp}", from_="+1234567890", to=phone
    )
    return otp
```

###### SendGrid (Email OTP):

- Install: pip install sendgrid

Use SendGridAPIClient to send email with OTP.
```python
Example:

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import random

def send_otp_email(email):
    otp = str(random.randint(1000, 9999))
    msg = Mail(
        from_email="your_email@example.com",
        to_emails=email,
        subject="Your OTP",
        html_content=f"Your OTP is {otp}"
    )
    SendGridAPIClient("API_KEY").send(msg)
    return otp
    ```