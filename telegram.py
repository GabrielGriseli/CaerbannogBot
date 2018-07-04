import telepot
from chatterbot import ChatBot

bot = ChatBot('Caerbannog', trainer="chatterbot.trainers.ChatterBotCorpusTrainer")

bot.train('chatterbot.corpus.portuguese')
bot.train("./history.yml")

telegram = telepot.Bot("SEU TOKEN")

def message(msg):
    response = bot.get_response(msg['text'])
    chatId = msg['chat']['id']
    if float(response.confidence) > 0.5:
        telegram.sendMessage(chatId, str(response))
    else:
        telegram.sendMessage(chatID, "Não entendi! Ainda estou aprendendo :)")

telegram.message_loop(message)

print("Press ctrl-c on the keyboard to exit")
while True:
    try:
        pass
    except (KeyboardInterrupt, EOFError, SystemExit):
        break