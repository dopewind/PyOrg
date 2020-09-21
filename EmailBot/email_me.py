
import smtplib
import time
import sys

email = 'imkvinayan@gmail.com'
pass_ = 'xssavsbezjdijojb'
_to = ''


def send_email(subject, msg, _to):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(email, pass_)
        message = 'Subject: {}\n\n{}'.format(subject, msg)
        server.sendmail(email, _to, message)
        server.quit()
        print("Success: Email sent!")
    except:
        print("Email failed to send.")


subject = ''
msg = ''
to = ''

print("Enter the command mode")
print('1. CI')
print('2. Send')
_mode = input("1 / 2 --> ")

if _mode == '1':
    print("Your wish is my command")
    task = input('--> ')

    name = ''

    print("Enter a name for the task")
    name = input('--> ')

    msg = '''"''' + name + '''"''' + ' finished running'
    subject = 'Dopewind CI'

    send_email(subject, msg, email)
elif _mode == '2':
    print('Enter subject for the email')
    subject = input('--> ')

    print("Ctrl - D to save")
    time.sleep(2)
    msg = sys.stdin.read()

    print('')

    print("To whom ?")
    _to = input('--> ')

    if _to == '':
        _to = email

    send_email(subject, msg, _to)
