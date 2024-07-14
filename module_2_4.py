from consoleTextStyle import ConsoleTextStyle as CTS
import math

digits_up_limit = 15
digits_list = [x+1 for x in range(digits_up_limit)]

primes = []
not_primes = []

print("Тыак, вроде всё собрал сколько там до выхода?..\nО, пятнадцать минут...")
CTS.colorful_text("-Дороу! Ты учил все простые числа до 15", CTS.Color.CYAN)
print("-...ЗАРАЗА!!!")
CTS.colorful_text("-Ну ты смотри, сегодня препод злой, так что тебе нужно чё-т придумать...\n"
                  "Эй! Где ты нашёл бутылку? Её ж только что у тебя в руках не было!", CTS.Color.CYAN)
print("-Это магия. Она работает перед уходом в запой.\n\nЛадн, придумаю чё-нить.")
print("\nПожалуй хакну мозг и напишу прогу для подсчёта простых чисел")

for digit_to_add in digits_list[1:]:
    for digit_to_check in range(2, int(math.ceil(digit_to_add/2))+1):
        if digit_to_add % digit_to_check == 0:
            not_primes.append(digit_to_add)
            break
    else:
        primes.append(digit_to_add)

CTS.colorful_text(f"\nПростые числа до {digits_up_limit}: {primes}", CTS.Color.BLUE)
CTS.colorful_text(f"Составные числа до {digits_up_limit}: {not_primes}", CTS.Color.BLUE)
print("\nО! Шик! Как раз в запой успею. Кстати...")
CTS.colorful_text(f"\nПеречень зависимостей тела...\n"
                  f"Удаляется зависимость от алкоголя...", CTS.Color.BLUE)
CTS.colorful_text(f"Ошибка! Не бухайте во время использования мозга!", CTS.Color.RED)
print("\nА, точно")
