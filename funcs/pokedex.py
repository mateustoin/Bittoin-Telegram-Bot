# Import das bibliotecas
from google_trans_new import google_translator 
import requests

class Pokedex(object):
    """[Resumo]
    A classe Pokedex possui todos os comandos referentes ao pokédex. 
    Pesquisa pelos pokemons podem ser tanto pelo nome quanto pelo número da pokédex.
    """
    def __init__(self):
        """[Resumo]
        Define URL base da API (pokeAPI) que será utilizada em todas as requisições.
        """
        self.url_base = 'https://pokeapi.co/api/v2/pokemon/'
    
    def pokedex(self, update, context):
        """[Resumo]
        Função executada quando o comando '/pokedex nome_do_pokemon' é utilizado no chat do telegram.
        """

        # Se quem acionou não colocar nenhum argumento no comando
        if not context.args:
            context.bot.send_message(chat_id=update.effective_chat.id, 
                                text='Esqueceu o nome ou número do pokemon!')
            return
        
        # Deixa palavra com letras minúsculas para realizar requisição
        pokemon = context.args[0].lower()
        
        requisicao = requests.get(url= self.url_base + pokemon)
        
        # Se a requisição deu errado, retorna mensagem de erro
        if (requisicao.status_code != 200):
            context.bot.send_message(chat_id=update.effective_chat.id, 
                                text='Nome ou número do pokemon incorreto, tente novamente!')

        # Se a requisição deu certo, coleta informações básicas do pokemon e envia
        else:
            num_pokedex = requisicao.json()['id']
            peso = requisicao.json()['weight']
            photo_url = requisicao.json()['sprites']['front_default']
            nome_pokemon = requisicao.json()['name'].capitalize()
            habilidades = ''
            
            for ab in requisicao.json()['abilities']:
                habilidades = habilidades + '- <i>' + ab['ability']['name'] + '</i>\n'
            
            context.bot.send_photo(chat_id=update.effective_chat.id,
                                photo=photo_url)
            
            context.bot.send_message(chat_id=update.effective_chat.id, 
                                    text='<b>Nome do Pokemon</b>: ' + nome_pokemon 
                                    + '\n<b>Peso do pokemon</b>: ' + str(peso)
                                    + '\n<b>Número na pokedéx</b>: ' + str(num_pokedex)
                                    + '\n<b>Habilidades</b>: \n' + str(habilidades),
                                    parse_mode='HTML')
            
    
    def habilidades(self, update, context):
        """[Resumo]
        Função executada quando o comando '/habilidades nome_do_pokemon' é utilizado no chat do telegram.
        """

        # Se quem acionou não colocar nenhum argumento no comando
        if not context.args:
            context.bot.send_message(chat_id=update.effective_chat.id, 
                                text='Esqueceu o nome do pokemon!')
            return
        
        # Deixa palavra com letras minúsculas para realizar requisição
        pokemon = context.args[0].lower()
        
        requisicao = requests.get(url= self.url_base + pokemon)
        
        # Se a requisição deu errado, retorna mensagem de erro
        if (requisicao.status_code != 200):
            context.bot.send_message(chat_id=update.effective_chat.id, 
                                text='Nome do pokemon incorreto, tente novamente!')

        # Se a requisição deu certo, coleta informações das habilidades, originalmente em inglês, traduz e envia
        else:
            descricao_habilidade = []
            nome_habilidade = []
            translator = google_translator() 
            
            for ab in requisicao.json()['abilities']:
                nome_habilidade.append(ab['ability']['name'])
                url_habilidade = ab['ability']['url']
                req_habilidade = requests.get(url=url_habilidade)
                
                for desc in req_habilidade.json()['effect_entries']:
                    if desc['language']['name'] == 'en':
                        descricao_traduzida = translator.translate(desc['effect'], lang_tgt='pt')
                        descricao_habilidade.append(descricao_traduzida)
                        break
                
            
            for it in range(len(nome_habilidade)):
                context.bot.send_message(chat_id=update.effective_chat.id, 
                                    text='Nome da Habilidade: ' + nome_habilidade[it] 
                                    + '\nDescrição: ' + descricao_habilidade[it])
            

    def moves(self, update, context):
        """[Resumo]
        Função executada quando o comando '/moves nome_do_pokemon' é utilizado no chat do telegram.
        """

         # Se quem acionou não colocar nenhum argumento no comando
        if not context.args:
            context.bot.send_message(chat_id=update.effective_chat.id, 
                                text='Esqueceu o nome do pokemon!')
            return
        
        # Deixa palavra com letras minúsculas para realizar requisição
        pokemon = context.args[0].lower()
        
        requisicao = requests.get(url= self.url_base + pokemon)
        
        # Se a requisição deu errado, retorna mensagem de erro
        if (requisicao.status_code != 200):
            context.bot.send_message(chat_id=update.effective_chat.id, 
                                text='Nome do pokemon incorreto, tente novamente!')

        # Se a requisição deu certo, coleta primeiros movimentos do pokemon e responde o usuário
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