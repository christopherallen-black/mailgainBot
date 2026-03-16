import os
from urllib.parse import urlparse
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
from telethon import TelegramClient

# ======= Your Credentials =======
BOT_TOKEN = "8760874913:AAH0a9Pm6CMIz4hD1GmUmeOrFefbBxyz0J4"        # From BotFather
api_id = 35554241                     # From my.telegram.org
api_hash = "c99833ecf6774ee619307094d6359bc6"          # From my.telegram.org
# ================================

download_folder = "downloads"
os.makedirs(download_folder, exist_ok=True)

# Telethon client
client = TelegramClient("session", api_id, api_hash)


async def download_media(link_or_username):
    """
    Downloads all media from a channel, group, or bot.
    """
    await client.start()
    
    # Clean the link to get username or invite
    parsed = urlparse(link_or_username)
    if parsed.netloc == "t.me":
        parts = parsed.path.strip("/").split("/")
        username = parts[0]  # channel/group username or joinchat
    else:
        username = link_or_username  # direct username or ID

    entity = await client.get_entity(username)

    async for message in client.iter_messages(entity):
        if message.media:
            file_path = await message.download_media(file=download_folder)
            if file_path:
                print("Downloaded:", file_path)


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    link = update.message.text.strip()

    await update.message.reply_text("Starting download... This may take a while for large channels.")

    try:
        await download_media(link)
        await update.message.reply_text(f"✅ Download completed! Files saved to `{download_folder}`")
    except Exception as e:
        await update.message.reply_text(f"❌ Error: {str(e)}")


# Telegram bot
app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT, handle_message))

print("Bot is running... Press Ctrl+C to stop")
app.run_polling()
