from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler
import os

app = Flask(__name__)

# 🔐 Token do seu bot
TOKEN = "7502454187:AAHXBG7M-nvcmZaVZ9nGr9VjNBzfZMpgPqY"
bot = Bot(token=TOKEN)

# 🔧 Dispatcher para lidar com comandos
dispatcher = Dispatcher(bot=bot, update_queue=None, workers=0)

# 👋 Comando /start
def start(update, context):
    update.message.reply_text("Olá! Eu sou o Agente32. Como posso ajudar?")

dispatcher.add_handler(CommandHandler("start", start))

# 📬 Rota principal para receber atualizações do Telegram
@app.route("/", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return "ok", 200

# 🚀 Rota para configurar o webhook (executar uma vez após deploy)
@app.route("/setwebhook", methods=["GET"])
def set_webhook():
    webhook_url = request.url_root  # Ex: https://bot-agente32.onrender.com/
    bot.set_webhook(url=webhook_url)
    return f"Webhook configurado para {webhook_url}", 200

if __name__ == "__main__":
    app.run(debug=True)



