#ᴀᴅᴅ ʟɪᴄᴇɴsᴇ ᴛᴇxᴛ ʜᴇʀᴇ ɢᴇᴛ ɪᴛ ғʀᴏᴍ ʙᴇʟᴏᴡ.

from MukeshRobot import pbot as mukesh # This is bot's client
from pyrogram import filters # pyrogram filters




import logging
from telegram import Update, ParseMode
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Replace 'YOUR_BOT_TOKEN' with the token you obtained from BotFather
bot_token = '6287631826:AAHkjzI_RV4qf1S9NYgFb5MCyVx-2hZ0S-0'

# Define a list to store authorized admin user IDs
authorized_admins = [1929914544]  # Replace with actual user IDs of authorized admins

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Function to handle the /start command
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Welcome to the broadcast module! Only authorized admins can use this feature.')

# Function to handle the /broadcast command
def broadcast(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    if user_id not in authorized_admins:
        update.message.reply_text("You are not authorized to use this feature.")
        return

    message = " ".join(context.args)
    if not message:
        update.message.reply_text("Please provide a message to broadcast.")
        return

    # Get a list of all chat IDs (groups and users) the bot is a member of
    all_chats = context.bot.get_chat_member(update.message.chat_id, context.bot.id).chat

    # Broadcast the message to all chats the bot is a member of
    for chat in all_chats:
        try:
            context.bot.send_message(chat.id, message, parse_mode=ParseMode.MARKDOWN)
        except Exception as e:
            logging.error(f"Failed to broadcast message to chat {chat.id}: {str(e)}")

# Function to handle unknown commands
def unknown(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Sorry, I don't understand this command.")

def main():
    updater = Updater(bot_token)
    dp = updater.dispatcher

    # Handlers for commands
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("broadcast", broadcast))

    # Handler for unknown commands
    dp.add_handler(MessageHandler(Filters.command, unknown))

    # Start the Bot
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
    #ғᴏʀ /help ᴍᴇɴᴜ
__mod_name__ = "Broadcast"
__help__ = "Broadcast"
