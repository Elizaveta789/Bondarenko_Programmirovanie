# Создайте класс «Студент», который имеет атрибуты имя, фамилия и оценки.
# Добавьте методы для вычисления среднего балла и определения, является ли студент
# отличником.

class Student:
    def __init__(self, first_name, last_name, marks):
        self.first_name = first_name
        self.last_name = last_name
        self.marks = marks

    def sred_arif_marks(self):
        return sum(self.marks) / len(self.marks)

    def result(self):
        return self.sred_arif_marks() >= 4.5


student1 = Student("Иван", "Петров", [5, 4, 5, 5, 4])
print(student1.first_name, student1.last_name, ", средний балл:", student1.sred_arif_marks())
print("Отличник?", 'Да' if student1.result() else 'Нет')
