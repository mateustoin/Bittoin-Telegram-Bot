from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

# Token do bot fornecido pelo @BotFather
from funcs.token_code import token

# Funcionalidades
from funcs.pokedex import Pokedex

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

class Bot(object):
    
    def __init__(self):
        bot_token = token
        
        self.updater = Updater(token=bot_token, use_context=True)
        self.dispatcher = self.updater.dispatcher
        
        self.pokedex = Pokedex()
        
    def run(self):
        start_handler = CommandHandler('start', self.start)
        pokedex_handler = CommandHandler('pokedex', self.pokedex.pokedex)
        habilidades_handler = CommandHandler('habilidades', self.pokedex.habilidades)
        moves_handler = CommandHandler('moves', self.pokedex.moves)
        
        self.dispatcher.add_handler(start_handler)
        self.dispatcher.add_handler(pokedex_handler)
        self.dispatcher.add_handler(habilidades_handler)
        self.dispatcher.add_handler(moves_handler)
        
        self.updater.start_polling()
        
        # Roda o bot até apertar CTRL + C ou receber um SIGNAL
        self.updater.idle()
        

    '''
        IMPLEMENTAÇÃO DOS COMANDOS
    '''
    def start(self, update, context):
        context.bot.send_message(chat_id=update.effective_chat.id, 
                                text="Bem vindo ao bot da transmissão (Ao vivo, não de covid)\nAcesse twitch.tv/bittoin para mais informações!")