from random import randint
from consoleTextStyle import ConsoleTextStyle as CTS


def check_as_divider(dividend: int,
                     divider: int) -> bool:
    return dividend % divider == 0


def find_the_password(lifeline: int) -> str:
    password = ""
    for first_term in range(1, lifeline - 1):
        for second_term in range(first_term + 1, lifeline):
            if check_as_divider(lifeline, first_term + second_term):
                password += str(first_term) + str(second_term)
    return password


if __name__ == "__main__":
    DOWN_LIMIT = 3
    UP_LIMIT = 20

    TEXT_TO_CHECK = """3 - 12
4 - 13
5 - 1423
6 - 121524
7 - 162534
8 - 13172635
9 - 1218273645
10 - 141923283746
11 - 11029384756
12 - 12131511124210394857
13 - 112211310495867
14 - 1611325212343114105968
15 - 1214114232133124115106978
16 - 1317115262143531341251161079
17 - 11621531441351261171089
18 - 12151811724272163631545414513612711810
19 - 118217316415514613712811910
20 - 13141911923282183731746416515614713812911
"""

    # Блок проверки логики
    result = ""
    for first_form in range(3, 21):
        second_form = find_the_password(first_form)
        result += f"{first_form} - {second_form}\n"
    CTS.colorful_text(CTS.ITALIC + "Логика работает корректно\n" if result == TEXT_TO_CHECK else
                      CTS.ITALIC + "Проблема с логикой\n",
                      CTS.Color.YELLOW)

    # Блок выполнения самого задания
    first_form = randint(DOWN_LIMIT, UP_LIMIT)
    second_form = find_the_password(first_form)

    print(f"Эти наркоманы вывели в первое поле число: {CTS.colorful_str(str(first_form), CTS.Color.BLUE)}\n"
          f"А могли вывести тебя... и не в поле, а нафиг отсюда... Странные они...\n"
          f"В любом случае не парься, держи пароль для второго поля:")
    CTS.colorful_text(second_form, CTS.Color.BLUE)
