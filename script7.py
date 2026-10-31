import random

class Cipher:
    def __init__(self, numbers):
        self.__numbers = numbers
        self.__result = self.__encrypt()

    def __encrypt(self):
        operation = random.choice(["+", "*", "-"])
        number = random.randint(1, 500)

        if operation == "+":
            result = sum(self.__numbers) + number
        elif operation == "*":
            result = sum(self.__numbers) * number
        else:
            result = sum(self.__numbers) - number

        return result

    def __str__(self):
        return f"Результат шифрування: {self.__result}"



numbers = list(map(int, input("Введіть числа через пробіл: ").split()))


cipher = Cipher(numbers)


print(cipher)

