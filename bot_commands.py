from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from get_json import get_dict_rates
from logger import log


def greeting_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'Hi, {update.effective_user.first_name}\nEnter /help to learn more')


def help_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'You can use the following command:\n/rate <the ticker you need(usd,eur etc)>')


def get_rate(update: Update, context: CallbackContext):
    log(update, context)
    rates_dict = get_dict_rates()
    msg = update.message.text
    msg = msg.replace('/rate ', '').lower().split(',')
    try:
        rate = rates_dict[msg[0].upper()]['Value']
        update.message.reply_text(f'{msg[0].upper()}={rate}')
    except:
        update.message.reply_text('Incorrect input')


if __name__ == '__main__':
    rates_dict = {
        'AUD': {'ID': 'R01010', 'NumCode': '036', 'CharCode': 'AUD', 'Nominal': 1, 'Name': 'Австралийский доллар',
                'Value': 40.8636, 'Previous': 40.1688},
        'AZN': {'ID': 'R01020A', 'NumCode': '944', 'CharCode': 'AZN', 'Nominal': 1, 'Name': 'Азербайджанский манат',
                'Value': 35.5215, 'Previous': 35.5908}}
    print(get_rate(rates_dict))
