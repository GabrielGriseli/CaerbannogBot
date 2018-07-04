from chatterbot import ChatBot

bot = ChatBot('Caerbannog', trainer="chatterbot.trainers.ChatterBotCorpusTrainer")

bot.train('chatterbot.corpus.portuguese')
bot.train("./history.yml")

print("Press ctrl-c on the keyboard to exit")
while True:
    try:
        quest = input("Você: ")
        response = bot.get_response(quest)
        if float(response.confidence) > 0.5:
            print("Caerbannog: ", response)
        else:
            print("Caerbannog: Não entendi! Ainda estou aprendendo :)")
    except (KeyboardInterrupt, EOFError, SystemExit):
        break