# Caerbannog

Um Chatterbot para tirar dúvidas sobre História Medieval

Este Chatterbot faz parte do trabalho de Inteligência Artificial do curso de
Ciência da Computação da Universidade Regional Integrada (URI) Campus Erechim.

Autor: Gabriel Júnior Griseli

Orientador: Prof Marcos A. Lucas

## Download do projeto

Olhe para o canto superior direito, aparecerá um botão para Download, você pode escolher entre:

### Donwload usando o git

Caso você tenha o git instalado basta digitar o seguinte comando:
```
git clone https://github.com/GabrielGriseli/CaerbannogBot.git
```
### Download .zip
Basta baixar o arquivo e extrair ele no seu computador

## Instalar Python versão 3.6.*

Para poder rodar o chatterbot você deve primeiro verificar se já possui o Python instalado. Para isso, digite no seu terminal o seguinte comando:
```
python -V
```

Caso a resposta seja positiva, você pode passar para o próximo tópico.

Caso contrário vá até o seguinte endereço https://www.python.org/downloads/ e busque pelo python versão 3.6.* compatível com o seu sistema operacional.

Para instalar e configurar o python você pode seguir um dos diversos tutoriais na internet.

Um bom tutorial para windows pode ser encontrado em https://python.org.br/instalacao-windows/.

## Instalar pacotes do projeto

O projeto vem com dois arquivos. O telegram.py usa o aplicativo Telegram para interagir com o chatterbot, já o terminal.py usa, obviamente, o terminal para comunicação com o chatterbot.

Para poder executar o projeto via Telegram é necessário ter instalados as bibliotecas chatterbot e telepot junto ao python. Para executar via terminal basta a biblioteca chatterbot.

O pacote chatterbot é uma biblioteca para criação de bots de conversação em python.

O pacote telepot irá fazer a comunicação entre o aplicativo Telegram e o nosso chatterbot Caerbannog.

```
pip install chatterbot
pip install telepot
```

## Criando o Chatterbot no Telegram

Primeiramente é necessário que você tenha uma conta no Telegram.

Após criar e acessar sua conta vá no campo **pesquisar** e procure pelo **@BotFather**.

O BotFather é o bot do Telegram que gerencia todos os bots criados, e é a partir dele que são criados e configurados todos os **chatbots**.

Iniciando uma conversa com o BotFather, digite o comando abaixo para dar início a criação do novo bot:
```
/newbot
```
O BotFather vai lhe perguntar o **nome** que você deve dar ao bot.

Depois o BotFather vai lhe perguntar o **username (deve ser único)** do seu bot. O **username** dos bots deve sempre terminar com a palavra *bot* no final. Por exemplo *TetrisBot* ou *tetris_bot*.

Criado o bot com sucesso, o BotFather vai gerar um **token** para o seu bot. Esse **token é único** e serve como uma "senha" para seu bot, portanto deve ser mantido em sigilo.

Caso tenha ficado com dúvida em algum comando basta digitar o comando abaixo que será apresentado lista de comandos para configurar o seu bot:
```
/help
```

## Configurando o chatterbot para comunicar-se ao Telegram

Após ter gerado o **token**, vá até a seguinte linha do código e cole seu **token**:
```
telegram = telepot.Bot("SEU TOKEN")
```

## Para executar o chatterbot usando o Telegram rode a seguinte linha de comando:
```
python telegram.py
```

## Para executar o chatterbot via terminal rode a seguinte linha de comando:
```
python terminal.py
```

Agora você já pode conversar com seu chattebot pelo Telegram ou via terminal.

## Algumas sentenças mapeadas

- Quando ocorreu a Idade Média?
- Alta Idade Média
- Baixa Idade Média
- Reinos Germânicos
- Reino Cristão dos Francos
- Império Bizantino
- Árabes e o Islamismo
- Feudalismo
- Nobreza
- Clero
- Servos
- Cruzadas
- Peste Negra

OBS: Nesta lista não conta todas as sentenças mapeadas, mas sim as principais.

## Referências

Cox, G. (2017). About chatterbot.

da Silva, B. C. D. (2006).  O estudo linguístico-computacional da linguagem. Letras de Hoje 41(2).

Russell, S. and Norvig, P. (2004). Inteligência artificial. CAMPUS - RJ.

Telegram. Telegram f.a.q.

Turing, A. M. (1950). Computing machinery and intelligence. Mind, 59(236):433–460.

Weizenbaum, J. (1966). Eliza—a computer program for the study of natural language communication between man and machine. Communications of the ACM, 9(1):36–45.

https://www.youtube.com/watch?v=EhphaG6bk0M&t=700s

https://www.youtube.com/watch?v=2TCkaJdcicQ