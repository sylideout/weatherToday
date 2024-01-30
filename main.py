import json

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

with open('api_keys.json') as api_keys_file:
    api_keys = json.load(api_keys_file)

TELEGRAM_TOKEN = api_keys.get('telegramToken')

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

app.add_handler(CommandHandler("hello", hello))

app.run_polling()
