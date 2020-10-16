import os       # Get env variables and run the given command
import sys      # Get arguments passed to the bot
import requests  # Send messages

# Getting the env variables
TOKEN = os.environ.get('BOT_TOKEN')
SERVER = os.environ.get('SERVER_MODE')


# The main function to send the message


def telegram_bot_sendtext(bot_message):

    bot_token = TOKEN
    bot_chatID = '1001518410'
    send_text = 'https://api.telegram.org/bot' + bot_token + \
        '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()


# Aliases
alias = {'ll': 'colorls -lA --sd',
         'lc': 'colorls -A --sd',
         'ls': 'colorls',
         'bazinga': 'sh /home/jinx/scripts/xfce4.sh',
         'dnsit': 'echo "nameserver 8.8.8.8" | sudo tee /etc/resolv.conf > /dev/null',
         'less': 'smartless',
         }


# Checking if it is running on CI server
if SERVER == 1 or SERVER == "1":
    msg = "Travis CI just made sure this works. Hoorayy 🚀"
    telegram_bot_sendtext(msg)
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
