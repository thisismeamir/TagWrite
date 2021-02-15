import telegram
import logging
from telegram.ext import Updater

bot = telegram.Bot(token='Token Goes Here!')

# See if you chosen the right bot:
# print(bot.get_me())


updater = Updater(token='Token Goes Here!', use_context=True)

#Sends Back Errors real-time
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
