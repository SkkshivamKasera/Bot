import telebot
import re

# Set your Telegram bot token here
TELEGRAM_BOT_TOKEN = "6418563359:AAEO4WdB-ksRAfFlX9GC-d9bzrG6HnrYbBc"

# Initialize the Telegram bot
bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

# Global dictionary to store the new caption text provided by users for each video
video_replacement_texts = {}

# Handler function to handle incoming video messages
@bot.message_handler(content_types=['video'])
def handle_video(message):
    try:
        # Check if the original message is a video and has a caption
        if message.caption is not None:
            # Get the current caption of the video
            current_caption = message.caption

            # Check if the caption contains "@" or "#" symbols
            if "@" in current_caption or "#" in current_caption:
                # Replace words starting with '@' and '#' with '@captain_moviess' in the current caption
                updated_caption = re.sub(r'@(\w+)|#(\w+)', '@captain_moviess', current_caption)
            else:
                # Add '[@captain_moviess]' to the beginning of the caption
                updated_caption = "[@captain_moviess] " + current_caption

            # Send the video back with the updated caption
            bot.send_video(message.chat.id, message.video.file_id, caption=updated_caption)

        else:
            bot.send_message(message.chat.id, "Sorry, the original message is not a video with a caption, and I cannot proceed.")

    except Exception as e:
        print(f"Error processing video: {e}")
        bot.reply_to(message, "Sorry, there was an error processing the video.")

# Polling to keep the bot running
bot.polling()
