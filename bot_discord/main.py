import discord
import asyncio
import random

# ============================================================
# CONFIGURAÇÕES — edite aqui antes de rodar
# ============================================================
TOKEN = "SEU_TOKEN_AQUI"          # Token do bot (Discord Developer Portal)
CHANNEL_ID = 123456789012345678   # ID do canal onde as mensagens serão enviadas
INTERVALO_SEGUNDOS = 60           # Tempo entre cada mensagem automática (em segundos)
# ============================================================

# Lista variada de mensagens
MENSAGENS = [
    # 🎉 Animadas / hype
    "🚀 Bora! Hoje é dia de ser produtivo!",
    "🔥 A galera tá on! O que tá rolando hoje?",
    "💪 Mais um dia, mais uma conquista. Vamos nessa!",
    "⚡ O servidor acordou! Bom dia a todos!",

    # 😂 Humor
    "🤖 Sou um bot, mas sinto que mereço um café também.",
    "🧠 Fato do dia: dormir é o melhor debug da vida.",
    "😅 Erro 404: motivação não encontrada. Mas tô aqui mesmo assim.",
    "🐛 Bug encontrado: segunda-feira. Aguardando hotfix.",
    "☕ Lembrete automático: hidrate-se. Agua > café. (Mentira, café forever.)",

    # 🎯 Frases motivacionais
    "✨ 'O sucesso é a soma de pequenos esforços repetidos dia após dia.' — R. Collier",
    "📚 Aprender algo novo hoje? Nunca é tarde demais.",
    "🎯 Foco. Consistência. Resultado. Simples assim.",
    "🌱 Todo expert já foi iniciante um dia. Continue.",

    # 🎮 Cultura gamer / dev
    "🎮 Save the game before the boss fight. Save your code before o deploy.",
    "💻 Código limpo hoje = menos sofrimento amanhã.",
    "🛠️ Não é bug, é feature não documentada.",
    "🧪 'Funciona na minha máquina' — o programador, eternamente.",

    # 🌙 Para diferentes horários
    "🌙 Boa noite, coders! Commit, push e dorme.",
    "☀️ Bom dia! O terminal tá esperando você.",
    "🌆 Boa tarde! Como tá o progresso de hoje?",

    # 🎲 Curiosidades aleatórias
    "🎲 Curiosidade: o primeiro bug de computador foi uma mariposa real encontrada em 1947.",
    "🌍 Python foi criado em 1991. Mais velho que muita gente aqui.",
    "🔢 'A' em ASCII é 65. Agora você sabe isso.",
    "📡 O Discord foi lançado em 2015. Jovem pra tanta responsabilidade.",
]


# Setup do bot
intents = discord.Intents.default()
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"✅ Bot conectado como: {client.user}")
    print(f"📡 Enviando mensagens no canal ID: {CHANNEL_ID}")
    print(f"⏱️  Intervalo: {INTERVALO_SEGUNDOS} segundos\n")
    client.loop.create_task(enviar_mensagens_automaticas())


async def enviar_mensagens_automaticas():
    await client.wait_until_ready()
    canal = client.get_channel(CHANNEL_ID)

    if canal is None:
        print("❌ Canal não encontrado! Verifique o CHANNEL_ID.")
        return

    while not client.is_closed():
        mensagem = random.choice(MENSAGENS)
        await canal.send(mensagem)
        print(f"📨 Mensagem enviada: {mensagem}")
        await asyncio.sleep(INTERVALO_SEGUNDOS)


client.run(TOKEN)