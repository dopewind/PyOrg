# imports

from twilio.rest import Client
import os


# variables

# --------------- Store these values in enviornment variables or enter them here ------------------

account_sid = os.environ['twilio_sid']
auth_token = os.environ['twilio_auth']
client = Client(account_sid, auth_token)


# functions

def notify_me(msg):
    message = client.messages.create(from_='whatsapp:+14155238886',
                                     body=msg,
                                     to='whatsapp:+919207461949')


# actions


print("Your wish is my command")
task = input('-->')

name = ''

print("Enter a name for the task")
name = input('-->')

done = 0

if done == 0:
    os.system(task)
    done += 1
    print('Task completed sucessfully')

if name == '':
    name = task

msg = '''"''' + name + '''"''' + ' finished running'

if done == 1:
    notify_me(msg)
