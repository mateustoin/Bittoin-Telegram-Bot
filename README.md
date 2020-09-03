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

# Ferramentas e recursos

<p id="estrutura" align='center'>
    <img src="https://github.com/mateustoin/Bittoin-Telegram-Bot/blob/master/img/2.png?raw=true">&nbsp;&nbsp;
</p>

<b>Em construção.</b>

<p id="todo" align='center'>
    <img src="https://github.com/mateustoin/Bittoin-Telegram-Bot/blob/master/img/3.png?raw=true">&nbsp;&nbsp;
</p>

Descrição das funcionalidades que o bot tem/terá.

<p id="pokedex" align='center'>
    <img src="https://github.com/mateustoin/Bittoin-Telegram-Bot/blob/master/img/4.png?raw=true">&nbsp;&nbsp;
</p>

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

<p id="uso" align='center'>
    <img src="https://github.com/mateustoin/Bittoin-Telegram-Bot/blob/master/img/5.png?raw=true">&nbsp;&nbsp;
</p>

<b>Em construção. Tudo sobre como usar o bot e afins</b>