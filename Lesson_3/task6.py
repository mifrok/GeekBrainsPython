"""
Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной
первой буквой. Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом. Каждое слово состоит
из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной
буквы. Необходимо использовать написанную ранее функцию int_func().
"""

def int_func(text):
    """Возвращает полученную строку, в которой каждое слово начинается с заглавной буквы"""
    if ' ' in text:
        text_list = text.split()
        for word in range(len(text_list)):
            text_list[word] = int_func(text_list[word])
        return ' '.join(text_list)
    return text.title()


user_input = input('Введите текст: ').lower()
print(f'Вы ввели {user_input}')
print(f'Результат - {int_func(user_input)}')



def test_int_func():
    """Тестирование работы функции"""
    text = 'aaa bbb ccc ddd'
    final_text = 'Aaa Bbb Ccc Ddd'
    text2 = 'ФФФ ДДД ЩЩЩ'
    final_text2 = 'Ффф Ддд Щщщ'
    text3 = '50'
    final_text3 = '50'
    print('Test - OK' if int_func(text) == final_text else 'Test - FAILED')
    print('Test - OK' if int_func(text2) == final_text2 else 'Test - FAILED')
    print('Test - OK' if int_func(text3) == final_text3 else 'Test - FAILED')

test_int_func()