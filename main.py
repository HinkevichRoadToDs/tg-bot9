from telegram import Update
from telegram.ext import Updater,CommandHandler
from bot_commands import greeting_command,help_command,get_rate

updater = Updater('token')


updater.dispatcher.add_handler(CommandHandler('start', greeting_command))
updater.dispatcher.add_handler(CommandHandler('help', help_command))
updater.dispatcher.add_handler(CommandHandler('rate', get_rate))

print('server start')
updater.start_polling()
updater.idle()
