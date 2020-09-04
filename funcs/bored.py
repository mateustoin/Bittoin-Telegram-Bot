# Importa bibliotecas
import requests
from googletrans import Translator
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

class Bored(object):
    """[Resumo]
    A classe Bored possui todos os comandos referentes ao desentediador. 
    """
    
    def __init__(self):
        """[Resumo]
        Método construtor define duas URL's. Uma utilizada para as requisições de atividades aleatórias
        e a outra para atividades específicas. Também é definida uma lista com todos as atividades possíveis
        para realizar as requisições de maneira mais fácil, pelo índice na lista relacionado com o botão clicado. 
        """
        self.url_base_random = 'http://www.boredapi.com/api/activity'
        self.url_base_specific = 'http://www.boredapi.com/api/activity?type='
        
        self.original_actions = ["education", "recreational", "social", 
                                 "diy", "charity", "cooking", 
                                 "relaxation", "music", "busywork"]
        
    def bored(self, update, context):
        """[Resumo]
        Função executada quando o comando '/bored' é utilizado no chat do telegram.
        """

        # Lista com as atividades traduzidas para exibir nos botões
        actions = ["Educacional", "Recreativa",
                   "Social", "DIY",
                   "Caridade", "Cozinha", 
                   "Relaxar", "Música", 
                   "Trabalho", "Random"]
        
        # Cria botões e define valor de callback para quando forem clicados
        keyboard = [[InlineKeyboardButton(actions[0], callback_data='0'),
                    InlineKeyboardButton(actions[1], callback_data='1')],
                    [InlineKeyboardButton(actions[2], callback_data='2'),
                    InlineKeyboardButton(actions[3], callback_data='3')],
                    [InlineKeyboardButton(actions[4], callback_data='4'),
                    InlineKeyboardButton(actions[5], callback_data='5')],
                    [InlineKeyboardButton(actions[6], callback_data='6'),
                    InlineKeyboardButton(actions[7], callback_data='7')],
                    [InlineKeyboardButton(actions[8], callback_data='8'),
                    InlineKeyboardButton(actions[9], callback_data='9')]]


        reply_markup = InlineKeyboardMarkup(keyboard)

        # Aciona botões com mensagem para escolher atividade
        update.message.reply_text('Por favor escolha um tipo de atividade:', reply_markup=reply_markup)
        
    def button(self, update, context):
        """[Resumo]
        Função acionada quando o botão é clicado. Define as requisições da API de acordo com o que foi 
        escolhido. Se for random aciona URL random, se for atividade específica aciona a URL relacionada
        às atividades.
        """
        query = update.callback_query

        # CallbackQueries need to be answered, even if no notification to the user is needed
        query.answer()

        if (int(query.data) <= 8):
            req_bored = requests.get(self.url_base_specific + self.original_actions[int(query.data)])
        else:
            req_bored = requests.get(self.url_base_random + '/')
        
        # Se requisição der errado, retorna mensagem de erro
        if (req_bored.status_code != 200):
            context.bot.send_message(chat_id=update.effective_chat.id, 
                                text='Requisição falhou, tente novamente!')
       
        # Se requisição deu certo, traduz atividade e envia para usuário
        else:
            translator = Translator()
            atividade_traduzida = req_bored.json()['activity']
            atividade_traduzida = translator.translate(atividade_traduzida, dest='pt').text
            num_participants = req_bored.json()['participants']
            
            del(translator)
            print('requisicao feita')
            query.edit_message_text(text=f"Atividade sugerida: {atividade_traduzida}\n" +
                                        f"Quantidade de participantes: {num_participants}")
        
        
    def participantes(self, update, context):
        """[Resumo]
        Função executada quando o comando '/participantes num_participantes' é utilizado no chat do telegram.
        """

        # Se não houver argumentos, retorna lembrete
        if not context.args:
            context.bot.send_message(chat_id=update.effective_chat.id, 
                                text='Esqueceu a quantidade de participantes!')
            return
        
        num_participants = int(context.args[0])
        
        # Alguns valores a API não tem retorno
        if (num_participants == 6 or num_participants == 7 or num_participants >= 9):
            context.bot.send_message(chat_id=update.effective_chat.id, 
                                text='Não existe atividade para essa quantidade de participantes!')
            return
        
        requisicao = requests.get(url= self.url_base_random + '?participants=' + str(num_participants))
        print(requisicao.json())
        
        # Se requisição der errado, retorna mensagem de erro
        if (requisicao.status_code != 200):
            context.bot.send_message(chat_id=update.effective_chat.id, 
                                text='Requisição falhou, tente novamente!')
        
        # Se requisição deu certo, traduz atividade e envia para usuário
        else:
            translator = Translator()
            atividade_traduzida = requisicao.json()['activity']
            atividade_traduzida = translator.translate(atividade_traduzida, dest='pt').text
            num_participants = requisicao.json()['participants']
            
            del(translator)
            print('requisicao feita')
            context.bot.send_message(chat_id=update.effective_chat.id, 
                                     text=f"Atividade sugerida: {atividade_traduzida}\n" +
                                          f"Quantidade de participantes: {num_participants}")