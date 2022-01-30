import telebot as tb
import generate_qr
import os
import config

bot = tb.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    print(message.chat.id)
    bot.send_message(message.chat.id, 'hi')





@bot.message_handler(content_types=['text'])
def qrcd(message):
    generate_qr.new_qr(id_msg=message.chat.id, url=message.text)
    filename = 'qrcods/' + str(message.chat.id) + '.png'
    for_send = open(filename, 'rb')
    bot.send_photo(message.chat.id, for_send)
    #os.remove(filename)

@bot.message_handler(content_types=['document'])
def dec(message):
    file_info = bot.get_file(message.document.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    filename = 'qrcods/' + str(message.chat.id) + '.png'
    with open(filename, 'wb') as new_file:
        new_file.write(downloaded_file)
    new_data = generate_qr.decoder_qr(message.chat.id)
    bot.reply_to(message, new_data)
   # os.remove(filename)

# @bot.message_handler(content_types=['photo'])
# def dec2(message):
#     file_info = bot.get_file(message.photo.file_id)
#     downloaded_file = bot.download_file(file_info.file_path)
#     filename = 'qrcods/' + str(message.chat.id) + '.png'
#     with open(filename, 'wb') as new_file:
#         new_file.write(downloaded_file)
#     new_data = generate_qr.decoder_qr(message.chat.id)
#     bot.reply_to(message, new_data)
#     os.remove(filename)



def main():
    bot.infinity_polling()

if __name__ == '__main__':
    main()