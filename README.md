<p id="introducao" align='center'>
    <img src="https://github.com/mateustoin/Bittoin-Telegram-Bot/blob/master/img/1.png?raw=true">&nbsp;&nbsp;
</p>

<p>
    Este bot multifuncional pode fazer de tudo um pouco! É uma pokedex, encurtador de URL e até te tira to tédio caso não tenha nenhuma ideia do que fazer. Foi desenvolvido na live do <a href="twitch.tv/bittoin">meu canal na twitch</a> com o objetivo de todos aprenderem diversas técnicas, funções e implementação de ideias dentro de apenas um projeto. Além disso, não coleta nenhum dado do usuário que interage com ele no Telegram, apenas responde com as requisições feitas.
</p>

<p>
    Abaixo você poderá ver quais API's e tecnologias foram utilizadas no projeto, instruções de instalação dos pacotes necessários e de uso da aplicação. O projeto foi finalizado e colocado para funcionar na nuvem, garantindo que todos possam usurfruir a qualquer momento. Basta adicionar <i>@BittoinLiveBot</i> no telegram e se divertir!
</p>

<p>
    A plataforma utilizada para rodar o bot na nuvem foi o <a href="https://www.heroku.com/">Heroku</a>, pois é rápido, simples e eficiente. O uso dessa plataforma não é obrigatório, tanto para testes do bot quanto para a execução na nuvem, pois ele pode rodar localmente na sua máquina ou outras plataformas podem ser utilizadas, como AWS, Google, entre outras.
</p>

<p>
    Lista de API's utilizadas no desenvolvimento do BOT:
</p>

<ol>
    <li> <a href="https://pokeapi.co/">PokéAPI (Pokédex aberto)</a>
    <li> <a href="https://rel.ink/">Relink (Encurtador de URL grátis)</a>
    <li> <a href="https://www.boredapi.com/">Bored API</a>
</ol>

<i>Fonte: <a href="https://github.com/public-apis/public-apis">Lista de API's públicas no Github</a></i>

<p>
    Principais pacotes python utilizados no desenvolvimento do BOT
</p>

<ol>
    <li> <a href="https://requests.readthedocs.io/en/master/">Requests</a>
    <li> <a href="https://python-telegram-bot.readthedocs.io/en/stable/">Python Telegram Bot</a>
    <li> <a href="https://pypi.org/project/googletrans/">Google Translate</a>
</ol>

> Versão python utilizada no projeto: Python 3.8

---

# Sumário
1. [Introdução](#introducao)
2. [Como o projeto está organizado](#estrutura)
3. [To-Do List das Funcionalidades](#todo)
    - [Pokédex](#pokedex)
4. [Como utilizar o Bot e Resultados](#uso)

# Instalação

<p>
    Para instalar os pacotes que foram utilizados nesse projeto e replicá-lo na sua máquina ou criar outro baseado nesse, algumas informações são necessárias para tudo dar certo! Primeiro, se quiser replicar em um bot próprio, será necessário criar seu bot lá no telegram, utilizando o chat do <code>@BotFather</code>. Nesse chat é possível criar um bot, editar comandos, adicionar descrição, etc. Mas o mais importante, para replicar o projeto, é salvar o <b>API Token</b> gerado na sua criação. Esse token pode ser colocado no arquivo <code>bot.py</code> no projeto, na variável <code>bot_token</code>, para que todas as funcionalidades rodem direto no seu bot.
</p>

<p>
    Existem duas formas de instalar tudo necessário para a execução do código, deverás escolher a que você achar melhor. Através do <code>requirements.txt</code> ou <code>Pipenv</code>. A configuração do bot na nuvem não será abordado aqui, visto que a própria documentação da plataforma utilizada (Heroku) tem o passo a passo para colocar o código rodando lá, mas vale a pena ressaltar que pelo menos um desses métodos de instalação de pacotes é necessário para a configuração do ambiente na nuvem, bem como no seu computador.
</p>

## Instalando pelo requirments.txt

<p>
    Instalar pelo requirments.txt é simples, pois só precisa ter o pip instalado na máquina e executar o seguinte comando:
</p>

> <code>pip install requirments.txt</code>

<p>
    A vantagem de instalar dessa forma é que é rápido, simples e fácil. Porém é necessário destacar que esse método garante apenas que as principais bibliotecas utilizadas no projeto sejam instaladas nas suas versões corretas, mas não suas sub dependências. Daqui há alguns anos talvez dê errado por isso, mas não precisa se preocupar.
</p>

## Istalando pelo Pipenv

<p>
    Para instalar os pacotes utilizando o Pipenv é simples, primeiro garanta que o Pipenv está estalado na sua máquina, com o seguinte comando:
</p>

> <code>pip install pipenv</code>

<p>Depois, instale os pacotes através do arquivo Pipfile.lock, com o comando:</p>

> <code>pipenv install --ignore-pipfile</code>

<p>Com tudo instalado, só precisará rodar o comando <i>pipenv shell</i> dentro da pasta do projeto e assim que estiver dentro do ambiente virtual com tudo instalado, executa o código normalmente.</p>

> <code>pipenv shell</code>
> 
> <code>python main.py</code>

---

# Ferramentas e recursos

<p id="estrutura" align='center'>
    <img src="https://github.com/mateustoin/Bittoin-Telegram-Bot/blob/master/img/2.png?raw=true">&nbsp;&nbsp;
</p>

<p>
    Nesse tópico será explicado como o projeto está estruturado, entre os arquivos e como os códigos se conectam, para que todos entendam e possam modificar da forma que for necessária. A forma de implementar é explicada já na própria documentação das bibliotecas, portanto o foco será na forma em que foi organizado neste projeto. Na figura a seguir é possível observar como os arquivos estão estruturados e a partir disso entraremos nas conexões entre eles (pasta img ignorada pois contém apenas as imagens utilizadas neste README).  
</p>

<p id="tree" align='center'>
    <img src="https://github.com/mateustoin/Bittoin-Telegram-Bot/blob/master/img/tree.png?raw=true">&nbsp;&nbsp;
</p>

<p>
    O projeto pode ser dividido em três seções:
    <ol>
        <li> <b>Códigos</b>: main.py e pasta funcs
        <li> <b>Exemplos</b>: pasta sample
        <li> <b>Pacotes</b>: Procfile, requirements.txt, Pipfile e Pipfile.lock
    </ol>
</p>

## Códigos

<p>
    Toda a organização do bot e códigos das funcionalidades estão dentro do diretório <code>funcs/</code>. O arquivo python <code>main.py</code> contém apenas a criação do objeto da classe <b>Bot</b> que está dentro de <code>bot.py</code> para realizar a execução do bot com a função <code>run()</code>.
</p>

<p>
    Cada funcionalidade criada para este projeto tem sua própria classe, <code>class Pokedex()</code>, <code>class Bored()</code> e <code>class Urlshort()</code>. Para manter o código organizado e fácil para manutenção, cada comando existente no bot está lotado nos métodos da classe. Na seção de uso do bot você deve notar que os nomes dos métodos são iguais aos nomes dos comandos do próprio bot, para que não haja confusões em relação a implementação de cada coisa. Como foram utilizadas algumas API's para a coleta de dados do bot, então cada classe também tem sua URL base, a fim de separar bem cada API e organizar suas respectivas requisições e particularidades. Um exemplo de implementação de comando pode ser visto a seguir, com o comando mais básico do bot, utilizando a função <code>send_message()</code> com o texto escrito, para a própria pessoa que chamou o comando.
</p>

```python
def start(self, update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Bem vindo ao bot da transmissão (Ao vivo, não de covid)\nAcesse twitch.tv/bittoin para mais informações!")
```

<p>
    Por último temos a classe principal do bot, no arquivo <code>bot.py</code>, que importa todas as classes de funcionalidades citadas anteriormente, cria seus respectivos objetos de classe e usa os métodos para gerenciar os comandos implementados e utilizados no chat do bot online. Depois que temos um objeto da classe da nossa funcionalidade, criamos um handler, onde serão passados o método que será chamado pelo bot e seu comando, como pode ser visto a seguir:
</p>

```python
pokedex_handler = CommandHandler('pokedex', self.pokedex.pokedex)
```

<p>
    O primeiro argumento é o nome do comando que será acionado no chat e o segundo o método que será chamado ao ser acionado. Após isso utilizamos o <code>dispatcher</code> do bot, que é responsável por gerenciar e fazer funcionar todos os handlers criados, a fim de responder a todas as requisições de usuários e manter a organização interna das chamadas. 
</p>

```python
self.dispatcher.add_handler(pokedex_handler)
```

<p>
    No final do processo temos a execução do bot propriamente dito, com todas as suas funcionalidades adicionadas ao <code>dispatcher</code> e aguarda pela finalização.
</p>

```python
# Inicia a execução do bot
self.updater.start_polling()

# Roda o bot até apertar CTRL + C ou receber um SIGNAL
self.updater.idle()
```

## Exemplos

<p>
    A pasta <code>sample/</code> possui os arquivos <b>sample.py</b> e <b>inlinekeyboard.py</b>. O <b>sample.py</b> possui os primeiros testes realizados no bot, no início da live, para testar como funcionam as funções da biblioteca de telegram para python, a fim de descobrir e validar algumas propriedades. Você pode notar que como está tudo em apenas um arquivo, fica bagunçado e difícil de separar, por isso a organização dos códigos em <code>funcs/</code> foi adotada. Em <b>inlinekeyboard.py</b> o exemplo foi retirado direto da documentação da biblioteca, com o objetivo de testar teclas/botões no chat do telegram, para implementar a função da Bored API.
</p>

## Pacotes

<p>
    A instalação dos pacotes já foi explicada anteriormente na seção de Instalações, portanto o foco será no arquivo <code>Procfile</code>. O Procfile é o que será executado na nuvem, através da plataforma <a href="https://www.heroku.com/">Heroku</a>. É um arquivo simples e contém o simples comando:
</p>

> worker: python main.py

<p>
    Este comando simplesmente aloca uma instância do servidor na nuvem (worker) para executar o nosso bot, através do arquivo <code>main.py</code>, que ativa a execução.
</p>

---

<p id="todo" align='center'>
    <img src="https://github.com/mateustoin/Bittoin-Telegram-Bot/blob/master/img/3.png?raw=true">&nbsp;&nbsp;
</p>

Aqui estão listados todas as funcionalidades que foram discutidas durante as lives, escritas e preenchidas. Cada um desses tópicos foi implementado e testado ao vivo. A ideia é que durante as lives o público ajuda na criação das funcionalidades, determinando os requisitos e como vai ficar no final.

## Funcionalidade: Ferramenta de pokédex

- [x] Imagem do pokemon
- [x] Número da pokedéx
- [x] Nome
- [x] Habilidades
- [x] Peso
- [x] Tratar erro se a pessoa colocou nome do pokemon errado
- [x] Colocar as habilidades e suas respectivas descrições em outro comando
- [x] Utilizar markdown para formatar o texto de saída
- [x] Listar/Filtrar os possíveis movimentos do pokemon
- [x] Pesquisar por número da pokédex

## Funcionalidade: Ferramenta pra te tirar do tédio

- [x] Criar a chamada do comando
- [x] Criar os botões para acionar o comando
- [x] Criar chamada para API a partir do tipo
- [x] Conectar cada chamada a seu respectivo botão
- [x] Organiza mensagem de saída para o usuário

## Funcionalidade: Encurtador de URL

- [x] Cria a chamada do comando
- [x] Realiza aquisição da URL através dos argumentos do comando
- [x] Realiza uma requisição na API com a URL
- [x] Organiza mensagem de saída para o usuário com a URL Encurtada

---

<p id="uso" align='center'>
    <img src="https://github.com/mateustoin/Bittoin-Telegram-Bot/blob/master/img/7.png?raw=true">&nbsp;&nbsp;
</p>

<p>
    Nesta seção serão mostrados os resultados obtidos com o bot e casos de uso para cada funcionalidade. Aproveite e adicione o bot no telegram e teste também! Basta procurar por <code>@BittoinLiveBot</code> e começar a digitar os comandos no chat.
</p>

<p>
    Se quiser ver uma demonstração completa e mais explicada de como tudo funciona, visita <a href="https://www.instagram.com/matteus_antonio/">meu Instagram</a> ou <a>meu canal do YouTube</a> que lá vai ter vídeos no IGTV/Canal com tudo e mais um pouco!
</p>

<p id="pokedex" align='center'>
    <img src="https://github.com/mateustoin/Bittoin-Telegram-Bot/blob/master/img/4.png?raw=true">&nbsp;&nbsp;
</p>

<p id="url" align='center'>
    <img src="https://github.com/mateustoin/Bittoin-Telegram-Bot/blob/master/img/5.png?raw=true">&nbsp;&nbsp;
</p>

<p id="bored" align='center'>
    <img src="https://github.com/mateustoin/Bittoin-Telegram-Bot/blob/master/img/6.png?raw=true">&nbsp;&nbsp;
</p>

---