import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(
    from_email = 'natsuki-mori@kke.co.jp',
    to_emails = 'natsuki-mori@kke.co.jp',
    subject = 'test',
    html_content = 'test'
)

sg = SendGridAPIClient(os.environ.get("SENDGRID_APIKEY"))
response = sg.send(message)
print(response.status_code)