from lib import fibonacci, bubble_sort, calculator
def tcalculator():
    try:
        assert calculator(3, 2, '+') == 5
        assert calculator(3, 2, '-') == 1
        assert calculator(3, 2, '*') == 6
        assert calculator(6, 2, '/') == 3
        print("Тест для функции calculator пройден")
    except AssertionError:
        print("Тест для функции calculator не пройден")

    try:
        calculator(3, 0, '/')  # Этот тест должен выбросить исключение
    except ValueError:
        print("Тест для функции calculator (деление на ноль) пройден")
    except Exception:
        print("Тест для функции calculator (деление на ноль) не пройден")

    try:
        calculator(3, 2, 'i')  # Этот тест должен выбросить исключение
    except ValueError:
        print("Тест для функции calculator (неверная операция) пройден")
    except Exception:
        print("Тест для функции calculator (неверная операция) не пройден")


def tfibonacci():
    try:
        assert fibonacci(1) == [0]
        assert fibonacci(2) == [0, 1]
        assert fibonacci(5) == [0, 1, 1, 2, 3]
        print("Тест для функции fibonacci пройден")
    except AssertionError:
        print("Тест для функции fibonacci не пройден")
    try:
        fibonacci(0)  # Этот тест должен выбросить исключение
    except ValueError:
        print("Тест для функции fibonacci (ошибочный ввод) пройден")
    except Exception:
        print("Тест для функции fibonacci (ошибочный ввод) не пройден")


def tbubble_sort():
    try:
        assert bubble_sort([4, 2, 7, 1]) == [1, 2, 4, 7]
        assert bubble_sort([]) == []
        assert bubble_sort([3]) == [3]
        print("Тест для функции bubble_sort пройден")
    except AssertionError:
        print("Тест для функции bubble_sort не пройден")
if __name__ == "__main__":
    tfibonacci()
    tbubble_sort()
    tcalculator()