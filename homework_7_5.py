import os
import time

for root, dirs, files in os.walk("."):
    for file in files:
        filepath = os.path.join(root, file)  # исправлено
        filetime = os.path.getmtime(os.path.join(root, file))  # исправлено
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(os.path.join(root, file))  # исправлено
        parent_dir = os.path.dirname(filepath)  # исправлено
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')