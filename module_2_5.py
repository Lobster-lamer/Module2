from consoleTextStyle import ConsoleTextStyle as CTS


def get_matrix(rows: int,
               columns: int,
               value_in_cells) -> list:
    matrix = []
    if rows <= 0 or columns <= 0:
        return matrix
    submatrix = []
    for column in range(columns):
        submatrix.append(value_in_cells)
    for row in range(rows):
        matrix.append(submatrix)
    return matrix


if __name__ == "__main__":
    CTS.colorful_text("Глеб, давай создадим матрицу!", CTS.Color.YELLOW)
    print("Давай!")
    print("\nИзвини, я совсем забыл спросить какая матрица тебе нужна, "
          "потому сделал код, который создаст любую простейшую, заполненную одинаковыми числами\n"
          "Вот смотри:\nВот тебе матрица 2 на 2, заполненная десятками:")
    CTS.colorful_text(get_matrix(2, 2, 10), CTS.Color.BLUE)
    print("Вот тебе матрица 3 на 5, заполненная числом 42:")
    CTS.colorful_text(get_matrix(3, 5, 42), CTS.Color.BLUE)
    print("Вот тебе матрица 4 на 2, заполненная числом 13:")
    CTS.colorful_text(get_matrix(4, 2, 13), CTS.Color.BLUE)
    print("Вот тебе матрица...")
    CTS.colorful_text("Глеб, ты опять что-то запрещённое употребил(осуждаю)?\n"
                      "Ты же сам после распада \"Агаты Кристи\" предложил создать новую группу Matrixx!",
                      CTS.Color.YELLOW)
    print("А, точно!)... А что с кодом делать?")
    CTS.colorful_text("Не знаю, отправь в Urban University, пусть по нему задание сделают",
                      CTS.Color.YELLOW)
