import os
from telegram import Update, BotCommand
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Get your Bot Token from environment variables
TOKEN = os.getenv("TOKEN")

# Bot commands
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = (
        "👋 Welcome to MailGain Bot!\n\n"
        "This bot helps you explore email buying and selling opportunities.\n\n"
        "Use the menu below:\n"
        "/buy - Learn how to buy emails\n"
        "/sell - Learn how to sell emails\n"
        "/contact - Contact support"
    )
    await update.message.reply_text(msg)

async def buy(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = (
        "📥 Buying Emails:\n"
        "- High-quality email lists available\n"
        "- Affordable pricing for businesses\n"
        "- Safe and verified contacts\n\n"
        "Contact us via /contact to start buying."
    )
    await update.message.reply_text(msg)

async def sell(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = (
        "📤 Selling Emails:\n"
        "- Sell your email lists safely\n"
        "- We connect you to buyers worldwide\n"
        "- Earn profit from verified leads\n\n"
        "Contact us via /contact to start selling."
    )
    await update.message.reply_text(msg)

async def contact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = (
        "📞 Contact Support:\n"
        "Email: support@mailgain.com\n"
        "Telegram: @mailgainSupport\n"
        "We respond within 24 hours."
    )
    await update.message.reply_text(msg)

# Main bot setup
app = ApplicationBuilder().token(TOKEN).build()

# Register command handlers
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("buy", buy))
app.add_handler(CommandHandler("sell", sell))
app.add_handler(CommandHandler("contact", contact))

# Optional: Set command menu for Telegram
async def set_commands(app):
    commands = [
        BotCommand("start", "Start the bot"),
        BotCommand("buy", "Learn how to buy emails"),
        BotCommand("sell", "Learn how to sell emails"),
        BotCommand("contact", "Contact support"),
    ]
    await app.bot.set_my_commands(commands)

app.run_polling(set_commands())
