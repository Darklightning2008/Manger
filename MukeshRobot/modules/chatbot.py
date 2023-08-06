import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
import os
import openai

# Set your ChatGPT API key here
openai.api_key = "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"

# Set your Telegram bot token here
TELEGRAM_BOT_TOKEN = "6287631826:AAHkjzI_RV4qf1S9NYgFb5MCyVx-2hZ0S-0"

# Define states for the conversation handler
START, CHAT = range(2)

# Callback function for the /start command
def start(update, context):
    update.message.reply_text("Hello! I'm your chatbot. Send /chat to start a conversation.")
    return CHAT

# Callback function to handle user messages
def chat(update, context):
    user_message = update.message.text
    chat_history = context.user_data.get("chat_history", [])
    
    # Add user message to the chat history
    chat_history.append(f"User: {user_message}")
    
    # Generate a response using ChatGPT
    response = openai.Completion.create(
        engine="davinci-codex",
        prompt="\n".join(chat_history),
        temperature=0.7,
        max_tokens=50
    )
    
    # Add the AI response to the chat history
    ai_response = response.choices[0].text.strip()
    chat_history.append(f"AI: {ai_response}")
    
    # Store the updated chat history in user data
    context.user_data["chat_history"] = chat_history
    
    # Send AI response to the user
    update.message.reply_text(ai_response)
    
    return CHAT

# Main function to run the bot
def main():
    updater = Updater(token=TELEGRAM_BOT_TOKEN, use_context=True)
    dp = updater.dispatcher
    
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            CHAT: [MessageHandler(Filters.text & ~Filters.command, chat)]
        },
        fallbacks=[]
    )
    
    dp.add_handler(conv_handler)
    
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
