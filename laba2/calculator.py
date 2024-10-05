def calculator(num1, num2, operation):
    """
    Функция выполняет арифметические операции с двумя числами.

    :param num1: Первое число
    :param num2: Второе число
    :param operation: Операция (+, -, *, /)
    :return: Результат операции
    """
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 == 0:
            raise ValueError("Деление на ноль!")
        return num1 / num2
    else:
        raise ValueError("Неверная операция")
