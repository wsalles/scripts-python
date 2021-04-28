import smtplib

FROM = 'Wallace Salles <wallace_robinson@hotmail.com>'
TO = ['user@gmail.com', 'user@hotmail.com']
SUBJECT = 'This is a simple Test'
MESSAGE = (f"""From: {FROM}
To: {TO}
Subject: {SUBJECT}
MIME-Version: 1.0
Content-Type: text/plain; charset=utf-8
Content-Disposition: inline
Content-Transfer-Encoding: 8bit

Hello everyone,
<YOUR MESSAGE>

Regards;
Wallace Salles
""")

try:
    mail = smtplib.SMTP('smtp.wallacesalles.dev', 25)
    mail.ehlo()
    # mail.starttls()
    # mail.login('', '')
    mail.sendmail(FROM, TO, MESSAGE.encode("utf8"))
    mail.close()
    print("Successfully sent email")
except Exception as e:
    print(f"Error: unable to send email. \n\nSee more details below: \n{e}")
