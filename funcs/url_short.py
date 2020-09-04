# Importa biblioteca
import requests

class Urlshort(object):
    """[Resumo]
    A classe Urlshort possui todos os comandos referentes ao encurtador de URL's. 
    """
    
    def __init__(self):
        """[Resumo]
        Define URL base da API (rel.ink) que será utilizada em todas as requisições.
        """
        self.url_base = 'https://rel.ink/api/links/'
        
    def url(self, update, context):
        """[Resumo]
        Função executada quando o comando '/url link_url' é utilizado no chat do telegram.
        """

        # Se quem acionou não colocar nenhum argumento no comando
        if not context.args:
            context.bot.send_message(chat_id=update.effective_chat.id, 
                                text='Coloque a URL depois do comando!')
            return
        
        # Constrói body com a url para enviar à API
        url = context.args[0]
        data = {
            "url": url
        }
        
        req_url = requests.post(self.url_base, data=data)
        
        # Se a requisição deu errado, retorna mensagem de erro
        if (req_url.status_code != 201):
            context.bot.send_message(chat_id=update.effective_chat.id, 
                                text='URL inválida! (Experimente com https:// ou http:// antes)')
            return
        
        # Se a requisição deu certo, coleta 'hashid' do encurtador e retorna URL pronta
        else:
            url_curta = 'https://rel.ink/' + req_url.json()['hashid']
            
            context.bot.send_message(chat_id=update.effective_chat.id, 
                                text='Sua url encurtada: ' + url_curta)
            print(req_url.json())