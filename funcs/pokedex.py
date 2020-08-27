from googletrans import Translator
import requests

class Pokedex(object):
    def __init__(self):
        self.url_base = 'https://pokeapi.co/api/v2/pokemon/'
    
    def pokedex(self, update, context):
        if not context.args:
            context.bot.send_message(chat_id=update.effective_chat.id, 
                                text='Esqueceu o nome do pokemon!')
            return
        
        pokemon = context.args[0]
        
        requisicao = requests.get(url= self.url_base + pokemon)
        
        if (requisicao.status_code != 200):
            context.bot.send_message(chat_id=update.effective_chat.id, 
                                text='Nome do pokemon incorreto, tente novamente!')
        else:
            num_pokedex = requisicao.json()['id']
            peso = requisicao.json()['weight']
            photo_url = requisicao.json()['sprites']['front_default']
            habilidades = ''
            
            for ab in requisicao.json()['abilities']:
                habilidades = habilidades + '- <i>' + ab['ability']['name'] + '</i>\n'
            
            context.bot.send_photo(chat_id=update.effective_chat.id,
                                photo=photo_url)
            
            context.bot.send_message(chat_id=update.effective_chat.id, 
                                    text='<b>Nome do Pokemon</b>: ' + pokemon 
                                    + '\n<b>Peso do pokemon</b>: ' + str(peso)
                                    + '\n<b>Número na pokedéx</b>: ' + str(num_pokedex)
                                    + '\n<b>Habilidades</b>: \n' + str(habilidades),
                                    parse_mode='HTML')
            
    
    def habilidades(self, update, context):
        if not context.args:
            context.bot.send_message(chat_id=update.effective_chat.id, 
                                text='Esqueceu o nome do pokemon!')
            return
        
        pokemon = context.args[0]
        
        requisicao = requests.get(url= self.url_base + pokemon)
        
        if (requisicao.status_code != 200):
            context.bot.send_message(chat_id=update.effective_chat.id, 
                                text='Nome do pokemon incorreto, tente novamente!')
            
        else:
            descricao_habilidade = []
            nome_habilidade = []
            translator = Translator()
            
            for ab in requisicao.json()['abilities']:
                nome_habilidade.append(ab['ability']['name'])
                url_habilidade = ab['ability']['url']
                req_habilidade = requests.get(url=url_habilidade)
                
                for desc in req_habilidade.json()['effect_entries']:
                    if desc['language']['name'] == 'en':
                        descricao_traduzida = translator.translate(desc['effect'], dest='pt').text
                        descricao_habilidade.append(descricao_traduzida)
                        break
                
            
            for it in range(len(nome_habilidade)):
                context.bot.send_message(chat_id=update.effective_chat.id, 
                                    text='Nome da Habilidade: ' + nome_habilidade[it] 
                                    + '\nDescrição: ' + descricao_habilidade[it])
            

    def moves(self, update, context):
        if not context.args:
            context.bot.send_message(chat_id=update.effective_chat.id, 
                                text='Esqueceu o nome do pokemon!')
            return
        
        #print('Requisição dos moves!')
        pokemon = context.args[0]
        #print('Pokemon: ' + pokemon)
        
        requisicao = requests.get(url= self.url_base + pokemon)
        
        if (requisicao.status_code != 200):
            context.bot.send_message(chat_id=update.effective_chat.id, 
                                text='Nome do pokemon incorreto, tente novamente!')
        else:
            moves = requisicao.json()['moves']
            move = []
            
            for mv in moves:
                move.append(mv['move']['name'])
            
            context.bot.send_message(chat_id=update.effective_chat.id, 
                                    text='Lista dos primeiros movimentos:')
            
            for index in range(5):
                context.bot.send_message(chat_id=update.effective_chat.id, 
                                        text=move[index])