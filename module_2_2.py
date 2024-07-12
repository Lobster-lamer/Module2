from consoleTextStyle import ConsoleTextStyle as CTS

print("Мудрец! Я шёл к Вам через пустыни и снега, через горы и равнины, "
      "я переплыл несколько морей и всё для того, чтобы услышать Вашу мудрость.")

CTS.colorful_text("Скажи мне три любых числа.", CTS.Color.YELLOW)

digits_to_compare = []
for digit_number in range(3):
    digits_to_compare.append(input(">>"))

equal_digits = 4 - len(set(digits_to_compare))

if equal_digits == 1:
    CTS.colorful_text("Ты не назвал ни одного повторяющегося числа", CTS.Color.YELLOW)
else:
    CTS.colorful_text(f"Ты назвал {equal_digits} повторяющихся числа", CTS.Color.YELLOW)

print("И это всё?")
CTS.colorful_text("Да", CTS.Color.YELLOW)
CTS.colorful_text("\n... Именно поэтому вы убили старого мудреца?", CTS.Color.BLUE)
