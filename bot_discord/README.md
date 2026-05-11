# Discord Auto Message Bot

Bot simples em Python que envia mensagens automáticas e aleatórias em um canal do Discord em intervalos configuráveis.

---

## Funcionalidades

- Envia mensagens automáticas em loop em um canal específico
- Escolha aleatória entre **25 mensagens variadas** pré-definidas
- Intervalo de envio totalmente configurável
- Log no terminal com cada mensagem enviada
- Validação do canal antes de começar o envio

---

## Estrutura do Projeto

```
discord-bot/
└── discord_bot.py   # Arquivo principal do bot
```

---

## ⚙️ Pré-requisitos

- Python 3.8 ou superior
- Biblioteca `discord.py`
- Uma conta no [Discord Developer Portal](https://discord.com/developers/applications)

---

## Instalação e Configuração

### 1. Clone ou baixe o repositório

```bash
git clone https://github.com/seu-usuario/discord-auto-bot.git
cd discord-auto-bot
```

### 2. Instale a dependência

```bash
pip install discord.py
```

### 3. Crie o bot no Discord Developer Portal

1. Acesse [discord.com/developers/applications](https://discord.com/developers/applications)
2. Clique em **New Application** e dê um nome ao bot
3. Vá em **Bot** → clique em **Add Bot**
4. Copie o **Token** do bot (guarde com segurança!)
5. Em **OAuth2 → URL Generator**, marque os escopos:
   - `bot`
   - Permissão: `Send Messages`
6. Use o link gerado para adicionar o bot ao seu servidor

### 4. Pegue o ID do canal

1. No Discord, ative o **Modo Desenvolvedor**:  
   `Configurações → Avançado → Modo Desenvolvedor`
2. Clique com botão direito no canal desejado
3. Selecione **Copiar ID**

### 5. Configure o arquivo `discord_bot.py`

Edite as três variáveis no topo do arquivo:

```python
TOKEN = "SEU_TOKEN_AQUI"          # Token copiado do Developer Portal
CHANNEL_ID = 123456789012345678   # ID do canal copiado do Discord
INTERVALO_SEGUNDOS = 60           # Tempo entre mensagens (em segundos)
```

---

## ▶️ Como Rodar

```bash
python discord_bot.py
```

Saída esperada no terminal:

```
✅ Bot conectado como: NomeDoBot#1234
📡 Enviando mensagens no canal ID: 123456789012345678
⏱️  Intervalo: 60 segundos

📨 Mensagem enviada: 🔥 A galera tá on! O que tá rolando hoje?
📨 Mensagem enviada: 🧠 Fato do dia: dormir é o melhor debug da vida.
```

---

## 💬 Categorias de Mensagens

O bot possui 25 mensagens divididas em 5 categorias:

| Categoria | Exemplos |
|---|---|
| 🎉 Animadas / Hype | "Bora! Hoje é dia de ser produtivo!" |
| 😂 Humor | "Erro 404: motivação não encontrada." |
| 🎯 Motivacionais | "Todo expert já foi iniciante um dia." |
| 🎮 Cultura Dev/Gamer | "Não é bug, é feature não documentada." |
| 🎲 Curiosidades | "O primeiro bug foi uma mariposa real, em 1947." |

Para adicionar novas mensagens, basta incluir strings na lista `MENSAGENS` no arquivo principal:

```python
MENSAGENS = [
    "Sua nova mensagem aqui! 🎉",
    # ...
]
```

---

## Personalização

| Variável | Padrão | Descrição |
|---|---|---|
| `TOKEN` | `"SEU_TOKEN_AQUI"` | Token de autenticação do bot |
| `CHANNEL_ID` | `123456789012345678` | ID do canal de destino |
| `INTERVALO_SEGUNDOS` | `60` | Segundos entre cada mensagem |

---

## Avisos

- **Nunca compartilhe seu Token** publicamente. Qualquer pessoa com o token pode controlar o bot.
- Evite intervalos muito curtos (menos de 10 segundos) para não correr o risco de o bot ser limitado pelo Discord (rate limit).
- O bot precisa estar online e rodando para enviar as mensagens. Considere usar um servidor ou ferramenta como [Railway](https://railway.app) ou [Replit](https://replit.com) para mantê-lo ativo 24/7.

---

## 🛠️ Tecnologias Utilizadas

- [Python 3](https://www.python.org/)
- [discord.py](https://discordpy.readthedocs.io/)
- [`asyncio`](https://docs.python.org/3/library/asyncio.html) — biblioteca nativa para programação assíncrona
- [`random`](https://docs.python.org/3/library/random.html) — biblioteca nativa para seleção aleatória

---

## 📄 Licença

Este projeto é livre para uso pessoal e educacional.
