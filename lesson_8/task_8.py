"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных
цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
    Если цифра есть на карточке - она зачеркивается и игра продолжается.
    Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
    Если цифра есть на карточке - игрок проигрывает и игра завершается.
    Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 87     - 14    11
      16 49    55 88    77
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html
"""
from random import choice, randint


class Keg:
    def __init__(self):
        self.numbers = [x for x in range(1, 91)]  # Drop pool

    def release_keg(self):
        number = choice(self.numbers)
        self.numbers.pop(self.numbers.index(number))
        print(f'Новый бочонок: {number:02} (осталось {len(self.numbers)})')
        return '{:02}'.format(number)


class LotoCard:
    def __init__(self, card):
        self.card = card

    def modify_loto_card(self, number):
        self.card = self.card.replace(number, '-' * len(number))
        for i in range(1, 10):  # Check if someone win
            if str(i) in self.card:
                break
            elif str(i) not in self.card and i == 9:
                print(self.card)
                return False
        return self.card

    def check_number_in_card(self, number):
        if number in self.card:
            return True
        else:
            return False

    @staticmethod
    def create_loto_card(card_name):
        pool_numbers = [x for x in range(1, 91)]
        list_numbers = [[pool_numbers.pop(pool_numbers.index(
            choice(pool_numbers))) for x in range(5)] for i in range(3)]
        # Take numbers from pool to matrix 5x3
        card = '{:-^30}'.format('Карточка игрока ' + card_name) + '\n'
        # First card string
        for i in list_numbers:
            i.sort()
        for i in list_numbers:
            for j in i:
                card += " " * randint(1, 4) + '{:02}'.format(j)
                # Transform to string
            card += '\n'
        card += '-' * 30  # fills last card string with "-"
        return card


def print_players_cards():
    print(player.card)
    print(computer.card)


def start_loto_game():
    input('Press any button to start game ')
    while True:
        try:
            number = keg.release_keg()
        except:
            print('Game over, both win')  # if all kegs are released
            break
        print_players_cards()
        if computer.check_number_in_card(number):  # computer auto play
            if not computer.modify_loto_card(number):  # win condition
                print('Все номера вычеркнуты, победа computer')
                return
        player_choice = input('Зачеркнуть цифру в карточке? (y/n) ')
        while player_choice != 'y' and player_choice != 'n':  # check input
            player_choice = input('Введите корректный ответ, "y" или "n": ')
        if player_choice == 'y':
            if player.check_number_in_card(number):
                if not player.modify_loto_card(number):  # win condition
                    print('Все номера вычеркнуты, победа Игрока!')
                    return
            else:
                print('Игрок ошибся, такого номера нет в карточке, проигрыш!')
                return  # if number in card, but player said NO
        else:
            if player.check_number_in_card(number):
                print('Игрок ошибся, такой номер есть в карточке, проигрыш!')
                return  # if number not in card, but player said YES
            else:
                continue


keg = Keg()
player = LotoCard(LotoCard.create_loto_card('Eugene'))
computer = LotoCard(LotoCard.create_loto_card('Computer'))
start_loto_game()
