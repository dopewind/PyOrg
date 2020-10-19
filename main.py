# --- Imports ---
import os  # Get env variables and run the given command
import sys  # Get arguments passed to the bot
import urllib.request  # To download the logs
from datetime import datetime  # Get Server time
import requests  # Send messages

# --- Env Variables ---
TOKEN = os.environ.get("BOT_TOKEN")
SERVER = os.environ.get("CI")
SERVER_OWN = os.environ.get("SERVER")
BUILD_LOG = os.environ.get("TRAVIS_JOB_WEB_URL")
HOME_PATH = os.environ.get("HOME")
BUILD_TYPE = os.environ.get("TRAVIS_EVENT_TYPE")
BUILD_BRANCH = os.environ.get("TRAVIS_BRANCH")
CURRENT_DIR = os.getcwd()


# --- Constants ---

# -- Time --
now = datetime.now()
current_time = now.strftime("%H:%M:%S")

# -- Aliases --
alias = {
    "ll": "colorls -lA --sd",
    "lc": "colorls -A --sd",
    "ls": "colorls",
    "bazinga": "sh /home/jinx/scripts/xfce4.sh",
    "dnsit": 'echo "nameserver 8.8.8.8" | sudo tee /etc/resolv.conf > /dev/null',
    "less": "smartless",
}

# --- Functions ---


def telegram_bot_sendtext(bot_message):

    bot_token = str(TOKEN)
    bot_chatID = "1001518410"
    send_text = (
        "https://api.telegram.org/bot"
        + bot_token
        + "/sendMessage?chat_id="
        + bot_chatID
        + "&parse_mode=Markdown&text="
        + bot_message
    )

    response = requests.get(send_text)

    return response.json()


def telegram_bot_senddocs(ab_local_url):
    bot_token = str(TOKEN)
    bot_chatID = "1001518410"
    files = {
        "chat_id": (None, bot_chatID),
        "document": (ab_local_url, open(ab_local_url, "rb")),
    }

    response = requests.post(
        "https://api.telegram.org/bot" + bot_token + "/sendDocument", files=files
    )
    return response


def get_logs(LOG_URL):
    print("Beginning log download...")
    DWL_PATH = HOME_PATH + "/log.txt"
    urllib.request.urlretrieve(LOG_URL, DWL_PATH)


# Checking if it is running on CI server
if SERVER == "true" or SERVER == True or SERVER_OWN == 1:

    BUILD_ID = BUILD_LOG[-9:]
    BUILD_LOG_URL = "https://api.travis-ci.com/v3/job/" + BUILD_ID + "/log.txt"

    print(
        SERVER_OWN,
        SERVER,
        BUILD_ID,
        BUILD_LOG_URL,
        BUILD_LOG,
        HOME_PATH,
        BUILD_TYPE,
        current_time,
    )

    get_logs(BUILD_LOG_URL)

    telegram_bot_sendtext("------------------")
    telegram_bot_sendtext("New build incoming")
    telegram_bot_sendtext("Current Server Time --> " + current_time)
    telegram_bot_sendtext("Build Type --> " + BUILD_TYPE)
    telegram_bot_sendtext("Current Build URL --> " + BUILD_LOG)
    telegram_bot_sendtext("Current build branch --> " + BUILD_BRANCH)
    telegram_bot_sendtext("Sending Logs 📩")
    telegram_bot_senddocs("/home/travis/log.txt")
    telegram_bot_sendtext("Travis CI just made sure this works. Hoorayy 🚀")
    telegram_bot_sendtext("------------------")
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
    print("")
    print("Task completed sucessfully")
    print("")

quote = 0
if name == "":
    name = task
    quote = 1

if quote == 0:
    msg = name + " finished running"
elif quote == 1:
    msg = '''"''' + name + '''"''' + " finished running"

if done == 1:
    telegram_bot_sendtext(current_time)
    print("Done!")

# -------------------------------------------------------------------------------------------
