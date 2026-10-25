name = input("Введіть своє ім'я: ")
age = int(input("Введіть свій вік: "))

print(f"Привіт {name}, тобі {age}!")

age = int(input("Введіть свій вік: "))

if age > 18:
    print("Вхід дозволено!")
else:
    print("Вхід заборонено!")

    import random

    number = random.randint(1, 50)
    attempts = 3

    print("Вгадай число від 1 до 50!")

    for i in range(attempts):
        guess = int(input("Введіть число: "))

        if guess == number:
            print("Вітаю! Ти вгадав число!")
            break
        elif guess > number:
            print("Менше")
        else:
            print("Більше")
    else:
        print(f"Спроби закінчилися! Загадане число: {number}")

        a = int(input("Введіть число, з якого почати: "))
        b = int(input("Введіть число, до якого виводити: "))

        for i in range(a, b + 1):
            print(i, end=" ")

            n = int(input("Введіть число n: "))

            for i in range(n, 1, -1):
                if i % 2 == 0:
                    print(i, end=" ")

                    n = int(input("Введіть число n: "))
                    factorial = 1

                    for i in range(1, n + 1):
                        factorial *= i

                    print(f"Факторіал числа {n} дорівнює {factorial}")

                    points = int(input("Введіть кількість балів: "))

                    if points < 0 or points > 100:
                        print("Некоректна кількість балів!")
                    elif points <= 49:
                        print("Незадовільно")
                    elif points <= 69:
                        print("Задовільно")
                    elif points <= 89:
                        print("Добре")
                    else:
                        print("Відмінно")