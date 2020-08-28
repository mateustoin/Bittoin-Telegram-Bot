import requests

class Urlshort(object):
    
    def __init__(self):
        self.url_base = 'https://rel.ink/api/links/'
        
    def url(self, update, context):
        if not context.args:
            context.bot.send_message(chat_id=update.effective_chat.id, 
                                text='Coloque a URL depois do comando!')
            return
        
        url = context.args[0]
        data = {
            "url": url
        }
        
        req_url = requests.post(self.url_base, data=data)
        
        if (req_url.status_code != 201):
            context.bot.send_message(chat_id=update.effective_chat.id, 
                                text='URL inválida! (Experimente com https:// ou http:// antes)')
            return
        
        else:
            url_curta = 'https://rel.ink/' + req_url.json()['hashid']
            
            context.bot.send_message(chat_id=update.effective_chat.id, 
                                text='Sua url encurtada: ' + url_curta)
            print(req_url.json())