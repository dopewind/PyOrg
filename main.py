# --- Imports ---
import os                       # Get env variables and run the given command
import sys                      # Get arguments passed to the bot
import requests                 # Send messages
import urllib.request           # To download the logs
from datetime import datetime   # Get Server time

# --- Env Variables ---
TOKEN = os.environ.get('BOT_TOKEN')
SERVER = os.environ.get('CI')
SERVER_OWN = os.environ.get('SERVER')
BUILD_LOG = os.environ.get('TRAVIS_JOB_WEB_URL')
HOME_PATH = os.environ.get('HOME')
BUILD_TYPE = os.environ.get('TRAVIS_EVENT_TYPE')

BUILD_ID = BUILD_LOG[-9:]
BUILD_LOG_URL = 'https://www.api.travis-ci.com/v3/job/' + BUILD_ID + '/log.txt'
print(SERVER_OWN, SERVER, BUILD_ID, BUILD_LOG_URL,
      BUILD_LOG, HOME_PATH, BUILD_TYPE)


# --- Constants ---

# -- Time --
now = datetime.now()
current_time = now.strftime("%H:%M:%S")

# -- Aliases --
alias = {'ll': 'colorls -lA --sd',
         'lc': 'colorls -A --sd',
         'ls': 'colorls',
         'bazinga': 'sh /home/jinx/scripts/xfce4.sh',
         'dnsit': 'echo "nameserver 8.8.8.8" | sudo tee /etc/resolv.conf > /dev/null',
         'less': 'smartless',
         }

# --- Functions ---


def telegram_bot_sendtext(bot_message):

    bot_token = TOKEN
    bot_chatID = '1001518410'
    send_text = 'https://api.telegram.org/bot' + bot_token + \
        '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()


def telegram_bot_senddocs(doc_url, caption):
    bot_token = TOKEN
    bot_chatID = '1001518410'
    send_docs = 'https://api.telegram.org/bot' + bot_token + \
        '/sendDocument?chat_id=' + bot_chatID + 'document=' + \
        doc_url + '&parse_mode=Markdown&caption=' + caption


def get_logs(LOG_URL):
    print('Beginning log download...')
    DWL_PATH = HOME_PATH + 'log.txt'
    urllib.request.urlretrieve(LOG_URL, DWL_PATH)


# Checking if it is running on CI server
if SERVER == 'true' or SERVER == True or SERVER_OWN == 1:
    msg = "Travis CI just made sure this works. Hoorayy 🚀"
    telegram_bot_sendtext(msg)
    telegram_bot_sendtext('Build Type --> ' + BUILD_TYPE)
    telegram_bot_sendtext('Current Build URL --> ', BUILD_LOG)
    telegram_bot_sendtext("Sending Logs 📩")
    telegram_bot_senddocs(BUILD_LOG_URL, current_time)
    exit(0)

# Arguments passed to the function
task = str(sys.argv[1])
name = str(sys.argv[2])


done = 0

task = str(task)

if done == 0:
    task = alias[task]

    os.system(task)
    done += 1
    print('')
    print('Task completed sucessfully')
    print('')

quote = 0
if name == '':
    name = task
    quote = 1

if quote == 0:
    msg = name + ' finished running'
elif quote == 1:
    msg = '''"''' + name + '''"''' + ' finished running'

if done == 1:
    telegram_bot_sendtext(msg)
    print('Done!')


# -------------------------------------------------------------------------------------------
