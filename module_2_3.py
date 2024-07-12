from consoleTextStyle import ConsoleTextStyle as CTS

print("Слуууушай! Тебе никто не говорил, что ты прям негативный человек и что, "
      "если б ты снимался в фильме, то был бы отрицательным персонажем?")
CTS.colorful_text("Нет, с чего бы это?", CTS.Color.BLUE)
print("Ну вот скажи мне пару чисел...")
CTS.colorful_text("Легко! Слушай:", CTS.Color.BLUE)
digits_of_antagonist = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index_of_antag_digits = 0
while 1:
    if (digits_of_antagonist[index_of_antag_digits] < 0 or
            index_of_antag_digits >= len(digits_of_antagonist)):
        break
    CTS.colorful_text(digits_of_antagonist[index_of_antag_digits], CTS.Color.BLUE)
    index_of_antag_digits += 1
print("Ладно, убедил... хоть бы одно отрицательное число сказал, вот же негативщик!")