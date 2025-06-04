class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def fullname(self):
        return print(f'{self.first} {self.last}')

    def code(self):
        print("I'm coding as an employee.")

class Developer(Employee):
    # Переопределение метода code()
    def code(self):
        print("I'm coding as a developer now!")


if __name__ == '__main__':

    dev_1 = Developer('Ivan', 'Ivanov', 60000)
    dev_1.fullname()  # Вызов метода базового класса Employee
    # Вывод: Ivan Ivanov
    dev_1.code()  # Вызов переопределенного метода класса Developer
    # Вывод: I'm coding as a developer now!
    dev_2 = Employee ('Sarah', 'Connor', 20000)
    dev_2.code()
