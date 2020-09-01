from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
import logging

# Token do bot fornecido pelo @BotFather
from funcs.token_code import token

# Funcionalidades
from funcs.pokedex import Pokedex
from funcs.url_short import Urlshort
from funcs.bored import Bored

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

class Bot(object):
    
    def __init__(self):
        bot_token = token
        
        self.updater = Updater(token=bot_token, use_context=True)
        self.dispatcher = self.updater.dispatcher
        
        self.pokedex = Pokedex()
        self.url_short = Urlshort()
        self.bored = Bored()
        
    def run(self):
        # Comandos básicos do bot
        start_handler = CommandHandler('start', self.start)
        
        # Comandos da pokédex
        pokedex_handler = CommandHandler('pokedex', self.pokedex.pokedex)
        habilidades_handler = CommandHandler('habilidades', self.pokedex.habilidades)
        moves_handler = CommandHandler('moves', self.pokedex.moves)
        
        # Comandos do encurtador de URL
        url_handler = CommandHandler('url', self.url_short.url)
        
        # Comandos do desentediador
        bored_handler = CommandHandler('bored', self.bored.bored)
        button_callback = CallbackQueryHandler(self.bored.button)
        participantes_handler = CommandHandler('participantes', self.bored.participantes)
        
        # Dispatchers do bot
        self.dispatcher.add_handler(start_handler)
        
        # Dispatchers da pokédex
        self.dispatcher.add_handler(pokedex_handler)
        self.dispatcher.add_handler(habilidades_handler)
        self.dispatcher.add_handler(moves_handler)
        
        # Dispatchers do encurtador de URL
        self.dispatcher.add_handler(url_handler)
        
        # Dispatchers do desentediador
        self.dispatcher.add_handler(bored_handler)
        self.dispatcher.add_handler(button_callback)
        self.dispatcher.add_handler(participantes_handler)
        
        # Inicia a execução do bot
        self.updater.start_polling()
        
        # Roda o bot até apertar CTRL + C ou receber um SIGNAL
        self.updater.idle()
        

    '''
        IMPLEMENTAÇÃO DOS COMANDOS
    '''
    def start(self, update, context):
        context.bot.send_message(chat_id=update.effective_chat.id, 
                                text="Bem vindo ao bot da transmissão (Ao vivo, não de covid)\nAcesse twitch.tv/bittoin para mais informações!")