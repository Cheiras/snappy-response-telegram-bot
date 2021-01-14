from telegram.ext import Updater, CommandHandler
from random import randrange


def get_url():
    urls = ['https://i.pinimg.com/236x/e2/c7/24/e2c724d12f43be3deb45cb9cdd71a892--futurama-meme-futurama-quotes.jpg',
            'https://lh3.googleusercontent.com/proxy/QhmdfXR0A0QsknF21MNGA1FzlhQtJ4vcsNOLNjx6PYVj7LiIAMRqMrcEMmrYe0NJD'
            'ACKUc4u2UljIf566NaCGs7h8nM_VJgVwYSjrsR3fdOzq5o'
            ]
    return urls[randrange(2)]


def snappy_response(update, context):
    url = get_url()
    chat_id = update.effective_chat.id
    context.bot.send_photo(chat_id=chat_id, photo=url)


def main():
    updater = Updater(token='YOUR_TOKEN', use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('snappy_response', snappy_response))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
