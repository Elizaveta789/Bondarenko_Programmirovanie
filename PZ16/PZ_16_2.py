# Создайте класс "Человек", который содержит информацию об имени, возрасте и поле.
# Создайте классы "Мужчина" и "Женщина", которые наследуются от класса
# "Человек". Каждый класс должен иметь метод, который выводит информацию о
# поле объекта

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_gender(self):
        print("Пол:", self.gender)


class Man(Person):
    def __init__(self, name, age):
        super().__init__(name, age, "Мужской")


class Woman(Person):
    def __init__(self, name, age):
        super().__init__(name, age, "Женский")


man1 = Man("Виталий", 50)
woman1 = Woman("Валерия", 25)

print(man1.name, man1.age, end='; ')
man1.show_gender()
print(woman1.name, woman1.age, end='; ')
woman1.show_gender()
