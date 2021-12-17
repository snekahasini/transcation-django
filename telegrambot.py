


from telegram.ext import * 


API_KEY = '5005616218:AAEjg10OvHIWM78gLF4J-3pButaAnD_szig'


def handle_message(update , context):
    text = str(update.message.text).lower()
    
    


         


    update.message.reply_text(f"Hi, trnscation complete")
    

if __name__ == '__main__':
    updater = Updater(API_KEY , use_context=True)
    dp = updater.dispatcher

    dp.add_handler(MessageHandler(Filters.text , handle_message))

    updater.start_polling(1.0)
    updater.idle()