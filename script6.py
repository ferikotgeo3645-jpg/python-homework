import random

class Room:
    def __init__(self, size):
        self.size = size
        self.dirt = random.randint(1, 10)

    def clean(self):
        if self.dirt > 0:
            self.dirt -= 1
            print("Робот прибрав бруд.")
        else:
            print("Кімната вже чиста!")

    def show_status(self):
        print(f"Рівень бруду в кімнаті: {self.dirt}")


class Robot:
    def __init__(self, name, room):
        self.name = name
        self.battery = 100
        self.room = room

    def work(self):
        while self.battery > 0 and self.room.dirt > 0:
            print(f"\nРобот {self.name} працює...")
            self.room.clean()
            self.battery -= 10
            print(f"Заряд батареї: {self.battery}%")

        if self.room.dirt == 0:
            print("\nПрибирання завершено!")
        else:
            print("\nБатарея розрядилася!")



room = Room(20)
robot = Robot("Робік", room)

# Запуск симуляції
print("Симуляція прибирання кімнати")
room.show_status()
robot.work()
room.show_status()

