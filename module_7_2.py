file_name = 'Emily Bronte_My soul is dark.txt'
with open(file_name, mode='rb') as file:
    file_content = file.read()
    text = file_content.decode('utf-8')
    print(text, '\n')

# Использование контекстного менеджера для открытия файла:
file_name = 'Emily Bronte_My soul is dark.txt'
with open(file_name, 'r', encoding='utf-8') as file:
    text = file.read()
    print(text, '\n')

# Чтение файла в одну строку:
file_name = 'Emily Bronte_My soul is dark.txt'
with open(file_name, 'r', encoding='utf-8') as file:
    print(file.read(), '\n')

# Чем отличается использование оператора with open(file_name...) от простого использования file.close()?

# 1. Автоматическое закрытие ресурсов: ключевое преимущество with - автоматическое закрытие ресурса (файла,
# соединения с базой данных и т.д.) после завершения блока with. Это гарантирует, что ресурс будет освобожден,
# даже если в коде произойдет ошибка. В противном случае необходимо вручную вызывать метод close(),
# что легко забыть, особенно в случае ошибок.
# 2. Упрощение кода: with делает код более кратким и читаемым, чем использование open() и close() отдельно.
# Код с with выглядит более логичным, так как ресурс открывается и закрывается в одном блоке.


# Пример
# Без with
file = open('Emily Bronte_My soul is dark.txt', 'r')
try:
    data_1 = file.read()
    # ... обработка данных
finally:
    file.close()

# С with
with open('Emily Bronte_My soul is dark.txt', 'r') as file:
    data_2 = file.read()
    # ... обработка данных
