import smtplib, ssl
import re
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_plain_text(sender_email, receiver_email, password, text):
    if verify_address(sender_email) == 'Bad Syntax':
        return 'Wrong sender email address'

    if verify_address(receiver_email) == 'Bad Syntax':
        return 'Wrong receiver email address'

    #sends HTML or plain text email
    message = MIMEMultipart("alternative")
    message["Subject"] = "multipart test"
    message["From"] = sender_email
    message["To"] = receiver_email

    # Create the plain-text and HTML version of your message

    html = f"""\
    <html>
    <body>
        <p>{text}
        </p>
    </body>
    </html>
    """

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )
    
    

def verify_address(email):
    addressToVerify = email
    match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', addressToVerify)

    if match == None:
        return 'Bad Syntax'
    else:
        return None