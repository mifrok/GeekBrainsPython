"""
*Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит информацию
об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами (характеристиками
товара: название, цена, количество, единица измерения). Структуру нужно сформировать программно, т.е. запрашивать
все данные у пользователя.
Пример готовой структуры:
[
    (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
    (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
    (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]
Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара, например
название, а значение — список значений-характеристик, например список названий товаров.
Пример:
{
    “название”: [“компьютер”, “принтер”, “сканер”],
    “цена”: [20000, 6000, 2000],
    “количество”: [5, 2, 7],
    “ед”: [“шт.”]
}
"""
goods = []  # Создание пустого списка
for i in range(int(input('Сколько товаров всего? '))):  # Формирование словаря с техникой
    my_dict = {
        'название': input(f'Введите название {i + 1} товара: '),
        'цена': input(f'Введите цену {i + 1} товара: '),
        'количество': input(f'Введите количество {i + 1} товара: '),
        'единица': input(f'Введите единицы измерения {i + 1} товара: '),
    }
    my_tuple = (i + 1, my_dict)  # Приведение к кортежу
    goods.append(my_tuple)  # Добавление элементов в пустой список
print(goods)
# Для реализации словаря используем доступ к уже имеющимся словарям в goods, с помощью генераторов списка
goods_analytics = dict(название=[goods[i][1]['название'] for i in range(len(goods))],
                       цена=[goods[i][1]['цена'] for i in range(len(goods))],
                       количество=[goods[i][1]['количество'] for i in range(len(goods))],
                       единица=[goods[i][1]['единица'] for i in range(len(goods))])
print(goods_analytics)