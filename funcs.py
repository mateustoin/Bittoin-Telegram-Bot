from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import telegram
import requests
import logging
import token_code

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

class Bot(object):
    
    def __init__(self):
        bot_token = token_code.token
        
        self.updater = Updater(token=bot_token, use_context=True)
        self.dispatcher = self.updater.dispatcher
        
    def run(self):
        start_handler = CommandHandler('start', self.start)
        pokedex_handler = CommandHandler('pokedex', self.pokedex)
        
        self.dispatcher.add_handler(start_handler)
        self.dispatcher.add_handler(pokedex_handler)
        
        self.updater.start_polling()
        

    '''
        IMPLEMENTAÇÃO DOS COMANDOS
    '''
    def start(self, update, context):
        context.bot.send_message(chat_id=update.effective_chat.id, 
                                text="Bem vindo ao bot da transmissão (Ao vivo, não de covid)\nAcesse twitch.tv/bittoin para mais informações!")
        
    def pokedex(self, update, context):
        print('Requisição do pokedex')
        pokemon = context.args[0]
        print('Pokemon: ' + pokemon)
        
        requisicao = requests.get(url='https://pokeapi.co/api/v2/pokemon/' + pokemon)
        
        num_pokedex = requisicao.json()['id']
        peso = requisicao.json()['weight']
        photo_url = requisicao.json()['sprites']['front_default']
        habilidades = ''
        
        for ab in requisicao.json()['abilities']:
            habilidades = habilidades + '- ' + ab['ability']['name'] + '\n'
        
        context.bot.send_photo(chat_id=update.effective_chat.id,
                               photo=photo_url)
        
        context.bot.send_message(chat_id=update.effective_chat.id, 
                                text='Nome do Pokemon: ' + pokemon 
                                + '\nPeso do pokemon: ' + str(peso)
                                + '\nNúmero na pokedéx: ' + str(num_pokedex)
                                + '\nHabilidades: \n' + str(habilidades))
        
bot = Bot()
bot.run()