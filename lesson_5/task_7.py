"""
Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать данные о
фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1   ООО   10000   5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила
убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.
"""
import statistics, json

firm_dict = {}
profit_dict = {'average_profit': []}
with open('task7.txt', 'r', encoding='utf-8') as task7:
    for i in task7.readlines():
        temp = i.split()
        temp.pop(1)  # Вырезаем лишнее значение (не требуется по условиям задачи)
        firm_dict[temp[0]] = int(temp[1]) - int(temp[2])  # Добавляем фирму с доходом\убытком в словарь
        if int(temp[1]) - int(temp[2]) >= 0:
            profit_dict['average_profit'].append(int(temp[1]) - int(temp[2]))  # Добавляем значение дохода\убытка в словарь
        # чтобы потом подсчитать среднее значение
profit_dict['average_profit'] = statistics.mean(profit_dict['average_profit'])  # подсчет среднего значения
new_list = [firm_dict, profit_dict]  #
with open('task7.json', 'w', encoding='utf-8') as task7:
    json.dump(new_list, task7)
