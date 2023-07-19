
import random
import configparser
from win_loss_kazino_logic import determine_outcome
def load_initial_money():
    config = configparser.ConfigParser()
    config.read('settings.ini')
    return int(config['DEFAULT']['MY_MONEY'])


def play_game():
    money = load_initial_money()
    slots = list(range(1, 31))

    while True:
        print(f"Ваш текущий капитал: ${money}")
        bet = int(input("Сделайте ставку: $"))

        if bet > money:
            print("У вас недостаточно средств.")
            continue

        selected_slot = int(input("Выберите номер слота (от 1 до 30): "))

        if selected_slot not in slots:
            print("Некорректный номер слота.")
            continue

        winning_slot = random.choice(slots)

        if selected_slot == winning_slot:
            money += bet * 2
            print(f"Вы выиграли! Ваш капитал увеличен до ${money}")
        else:
            money -= bet
            print(f"Вы проиграли! Ваш капитал уменьшен до ${money}")

        play_again = input("Хотите сыграть еще? (да/нет): ")

        if play_again.lower() != 'да':
            break

    print("Игра окончена.")
    print(f"Ваш конечный капитал: ${money}")
    if money > load_initial_money():
        print("Вы выиграли!")
    elif money < load_initial_money():
        print("Вы проиграли.")
    else:
        print("Вы закончили игру с тем же капиталом, с которым начали.")
