"""
Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.
"""
my_str = input('Введите несколько слов через пробел: ')
my_list = my_str.split(' ')
for word in range(len(my_list)):
    if len(my_list[word]) >= 10:
        print(f' {word+1}: {my_list[word][:10]}')
    else:
        print(f' {word+1}: {my_list[word]}')