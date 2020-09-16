import telepot
token = '
TelegramBot = telepot.Bot(token)
print (TelegramBot.getMe())
def hand(msg):
   content_type, chat_id=telepot.glance(msg)
   print(content_type, chat_type, chat_id)
   
   if content_type == "text':
          TelegramBot.sendMessage(chat_id, "You said'{}'",format (msg)["text"])}))
    
    TelegramBot.Message_loop(handle)
