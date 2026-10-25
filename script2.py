import random


class Student:
    def __init__(self, name="Ralf"):
        self.name = name
        self.money = 150  # Баланс денег
        self.progress = 50  # Успеваемость (0-100)
        self.satiety = 60  # Сытость / Здоровье (0-100)
        self.attendance = 80  # Процент посещаемости лекций (0-100)
        self.alive = True

    def info(self, day):
        print(f"\n================ СТАТУС: ДЕНЬ {day} ================")
        print(f" Студент: {self.name}")
        print(f" Гроші: {self.money}$ | Навчання (Успеваемость): {self.progress}/100")
        print(f" Ситість: {self.satiety}/100 | Відвідуваність лекцій: {self.attendance}%")
        print("==================================================")

    def morning_event(self):
        """Случайное событие при пробуждении"""
        event = random.choice(["good", "bad", "neutral"])
        if event == "good":
            print(f" Утро: {self.name} проснулся полным сил! (+10 к сытости)")
            self.satiety = min(100, self.satiety + 10)
        elif event == "bad":
            print(f" Утро: {self.name} проспал будильник и чувствует себя разбитым.")
            self.satiety = max(0, self.satiety - 10)
        else:
            print(f" Утро: Обычное утро. {self.name} заварил кофе и готов к выбору дня.")

    # --- Действия ---
    def go_to_lecture(self):
        print(f" {self.name} пошёл на лекции. Преподаватели довольны!")
        self.progress = min(100, self.progress + 15)
        self.attendance = min(100, self.attendance + 10)
        self.satiety = max(0, self.satiety - 15)

    def skip_lecture(self):
        print(f" {self.name} прогулял лекции. Деканат начинает что-то подозревать...")
        self.attendance = max(0, self.attendance - 15)
        self.progress = max(0, self.progress - 5)
        self.satiety = min(100, self.satiety + 5)  # немного отдохнул

    def work(self):
        print(f"{self.name} пошёл работать на подработку.")
        self.money += 60
        self.satiety = max(0, self.satiety - 20)
        self.progress = max(0, self.progress - 5)

    def eat(self):
        if self.money >= 15:
            print(f" {self.name} вкусно поел в столовой (-15$).")
            self.money -= 15
            self.satiety = min(100, self.satiety + 30)
        else:
            print(f" У {self.name} нет денег на нормальную еду! Пришлось грызть сухой паёк.")
            self.satiety = min(100, self.satiety + 5)

    def chill(self):
        if self.money >= 20:
            print(f" {self.name} пошёл зависать с друзьями в клубе (-20$).")
            self.money -= 20
            self.satiety = min(100, self.satiety + 15)
            self.progress = max(0, self.progress - 10)
        else:
            print(f" Денег нет. {self.name} просто посидел в телефоне дома.")
            self.satiety = min(100, self.satiety + 10)

    def check_state(self):
        """Проверка критических условий вылета/проигрыша"""
        if self.satiety <= 0:
            print(f"\n !!! {self.name} упал в голодный обморок и попал в больницу. Симуляция окончена !!!")
            self.alive = False
        elif self.attendance < 30:
            print(f"\n !!! {self.name} отчислен за огромные прогулы (посещаемость ниже 30%)! !!!")
            self.alive = False
        elif self.progress <= 0:
            print(f"\n !!! {self.name} отчислен за полную неуспеваемость! !!!")
            self.alive = False


# --- Основной цикл программы ---
def main():
    print(" ДОБРО ПОЖАЛОВАТЬ В СИМУЛЯТОР СТУДЕНТА ")
    name_input = input("Введите имя студента (или нажмите Enter для 'Ralf'): ")
    student = Student(name_input if name_input else "Ralf")

    days_in_year = 365

    for day in range(1, days_in_year + 1):
        if not student.alive:
            break

        student.info(day)
        student.morning_event()

        # Меню выбора действий для проверяющего
        print("\nЧто делать студенту сегодня?")
        print("1. Пойти на лекции ()")
        print("2. Прогулять лекции ()")
        print("3. Пойти работать / заработать денег ()")
        print("4. Поесть ()")
        print("5. Отдохнуть / Развлечься ()")
        print("0. Закончить симуляцию преждевременно (Выход)")

        while True:
            choice = input("Выберите номер действия: ").strip()

            if choice == "1":
                student.go_to_lecture()
                break
            elif choice == "2":
                student.skip_lecture()
                break
            elif choice == "3":
                student.work()
                break
            elif choice == "4":
                student.eat()
                break
            elif choice == "5":
                student.chill()
                break
            elif choice == "0":
                print("Симуляция завершена пользователем.")
                return
            else:
                print("Неверный ввод. Пожалуйста, выберите цифру от 0 до 5.")

        # Проверяем состояние после выбранного действия
        student.check_state()

        # Небольшая пауза между днями для визуального разделения
        input("\nНажмите Enter, чтобы перейти к следующему дню...")

    if student.alive:
        print(f"\n ПОЗДРАВЛЯЕМ! {student.name} успешно пережил этот учебный год! ")


if __name__ == "__main__":
    main()

