from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# Inserisci il tuo token
TOKEN = "8155219123:AAFs5xunHkSUsKTp3TIpFelZx1hUEeD7MJI"

async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Ciao! Sono un bot Telegram.")

async def echo(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(update.message.text)

def main():
    app = Application.builder().token(TOKEN).build()

    # Aggiungi i gestori di comandi e messaggi
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Avvia il bot
    print("Bot avviato...")
    app.run_polling()

if __name__ == "__main__":
    main()
