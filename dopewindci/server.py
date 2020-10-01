from bot import telegram_chatbot
import os

# ==================== aliases ============================


alias = ['ll', 'lc', 'ls', 'bazinga', 'dnsit', 'less', 'churn']


# ====================== config ============================

bot = telegram_chatbot("config.cfg")

# ============================== function ==================


def make_reply(msg):
    try:
        print("Message is", msg)
        reply = None
        output = None
        send_ = 0
        if msg is not None:
            if msg[0] == '/':

                # ============== /run ==========================
                if msg == '/run':
                    reply = 'Run what?'
                elif msg[1:4] == 'run' and msg[4] == ' ':
                    command = msg[5:]
                    if command in alias:
                        if command == 'll':
                            command = 'colorls -lA --sd'
                        elif command == 'lc':
                            lc = 'colorls -A --sd'
                        elif command == 'ls':
                            ls = 'colorls'
                        elif command == 'bazinga':
                            bazinga = 'sh /home/jinx/scripts/xfce4.sh'
                        elif command == 'dnsit':
                            dnsit = 'echo "nameserver 8.8.8.8" | sudo tee /etc/resolv.conf > /dev/null'
                        elif command == "less":
                            less = 'smartless'
                        elif command == 'churn':
                            churn = 'bash tools/run.sh --trace'
                    else:
                        command = str(command)
                    print('Final command is', command)
                    error = ''
                    error = os.system(command + ' > output.txt')
                    if error == 0:
                        send_ = 1
                        f = open("output.txt", "r")
                        output = f.read()
                        reply = 'Command completed'
                    elif error != 0:
                        f = open("output.txt", "r")
                        send_ = 1
                        f.seek(0)
                        output = str(error)
                        reply = "Command failed"
                    print(output)
                    f.close()
                # =============== /help =======================
                elif msg == '/help':
                    reply = '''
                            @dopewindcibot by @dopewind

/start to use the most useless command
/run to run commands on the host
/help to print this

                            '''
            # ================ future stuff ================

        elif msg is None:
            reply = "That ain't gonna work here chief"
        if send_ == 1:
            bot.send_message("Sending output", from_)
            bot.send_message(output, from_)
            send_ = 0
        return reply
    except KeyboardInterrupt:
        exit()
# ====================== loop ======================


update_id = None
while True:
    updates = bot.get_updates(offset=update_id)
    updates = updates["result"]
    if updates:
        for item in updates:
            update_id = item["update_id"]
            try:
                message = str(item["message"]["text"])
            except:
                message = None
            try:
                from_ = item["message"]["from"]["id"]
            except KeyError:
                from_ = '1001518410'
            reply = make_reply(message)
            bot.send_message(reply, from_)
