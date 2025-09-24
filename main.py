import math

def calculator():
    print("=== калькулятор ===")
    print("операции:")
    print("1. сложение (+)")
    print("2. вычитание (-)")
    print("3. умножение (*)")
    print("4. деление (/)")
    print("5. возведение в степень (**)")
    print("6. извлечение квадратного корня (sqrt)")
    print("7. остаток от деления (%)")
    print("8. выход")

    while True:
        choice = input("\nвыберите операцию (1-8): ")

        if choice == "8":
            print("выход из программы. спасибо!")
            break

        try:
            if choice == "6":  
                num = float(input("введите число: "))
                if num < 0:
                    print("ошибка: нельзя извлечь корень из отрицательного числа.")
                else:
                    print(f"√{num} = {math.sqrt(num)}")

            else:
                num1 = float(input("введите первое число: "))
                num2 = float(input("введите второе число: "))

                if choice == "1":
                    print(f"результат: {num1} + {num2} = {num1 + num2}")
                elif choice == "2":
                    print(f"результат: {num1} - {num2} = {num1 - num2}")
                elif choice == "3":
                    print(f"результат: {num1} * {num2} = {num1 * num2}")
                elif choice == "4":
                    if num2 == 0:
                        print("ошибка: деление на ноль!")
                    else:
                        print(f"результат: {num1} / {num2} = {num1 / num2}")
                elif choice == "5":
                    print(f"результат: {num1} ** {num2} = {num1 ** num2}")
                elif choice == "7":
                    if num2 == 0:
                        print("ошибка: деление на ноль!")
                    else:
                        print(f"результат: {num1} % {num2} = {num1 % num2}")
                else:
                    print("неверный выбор операции.")

        except ValueError:
            print("ошибка: введите корректное число!")

calculator()
