file_name = 'Emily Bronte_My soul is dark.txt'
file = open(file_name, mode='rb')  # Открываем файл в режиме "rb" (байтовое чтение)
file_content = file.read()  # Читаем все содержимое файла в виде байтов
text = file_content.decode('utf-8')  # Декодируем байты в строку с помощью utf-8
print(text)  # Выводим строку в консоль
file.close()  # Закрываем файл

# или так:
# file_name = 'Emily Bronte_My soul is dark.txt'
# with open(file_name, mode='rb') as file:  # Используем 'with' для автоматического закрытия файла
#     file_content = file.read()
#     text = file_content.decode('utf-8')
#     print(text)
