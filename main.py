from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import token_code

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

# Insira aqui o token do seu bot!
bot_token = token_code.token

updater = Updater(token=bot_token, use_context=True)

dispatcher = updater.dispatcher

help_message = '/start - Mensagem de boas vindas\n'
help_message = help_message + '/caps - Toda a mensagem depois do comando fica maiúscula\n'
help_message = help_message + '/image - Envia foto de um robô tocando teclado\n'

def help(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, 
                             text=help_message)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, 
                                text="Bem vindo ao bot da transmissão (Ao vivo, não de covid)\nAcesse twitch.tv/bittoin para mais informações!")

def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text + '!')

def caps(update, context):
    print(context.args)
    text_caps = ' '.join(context.args).upper()
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)

def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Me desculpe, desconheço este comando.")

def image(update, context):
    context.bot.send_photo(chat_id=update.effective_chat.id, 
                   photo=open('Mateus-Antonio-IoT-robotica-programação.jpg', 'rb'))

image_handler = CommandHandler('image', image)
help_handler = CommandHandler('help', help)
caps_handler = CommandHandler('caps', caps)
echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
start_handler = CommandHandler('start', start)
unkown_handler = MessageHandler(Filters.command, unknown)

dispatcher.add_handler(image_handler)
dispatcher.add_handler(help_handler)
dispatcher.add_handler(caps_handler)
dispatcher.add_handler(echo_handler)
dispatcher.add_handler(start_handler)

# Adicionado por último para dar chance do comando ser acionado se existir
dispatcher.add_handler(unkown_handler)

updater.start_polling()