import requests
import sys
import os


def telegram_bot_sendtext(bot_message):

    bot_token = '1185740681:AAG_H3nxkveqKBdl4z1-MCgA80Zln3Mpk3E'
    bot_chatID = '1001518410'
    send_text = 'https://api.telegram.org/bot' + bot_token + \
        '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()


task = str(sys.argv[1])
name = str(sys.argv[2])

done = 0

if done == 0:
    os.system(task)
    done += 1
    print('')
    print('Task completed sucessfully')
    print('')

if name == '':
    name = task

msg = '''"''' + name + '''"''' + ' finished running'

if done == 1:
    test = telegram_bot_sendtext(msg)
    print('Done!')
