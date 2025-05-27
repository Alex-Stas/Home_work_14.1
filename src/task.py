import datetime

class Task:
    name: str
    description: str
    status: str
    created_at: str

    def __init__(self, name, description, status='Ожидает старта', created_at=None):
        self.name = name
        self.description = description
        self.status = status
        self.__created_at = created_at if created_at else datetime.date.today().strftime('%d.%m.%Y')

    @classmethod
    def new_task(cls, name, description, status='Ожидает старта', created_at=None):
        return cls(name, description, status, created_at)

    @property
    def created_at(self):
        return self.__created_at

    @created_at.setter
    def created_at(self, new_date: str):
        if datetime.datetime.strptime(new_date, '%d.%m.%Y').date() < datetime.datetime.now().date():
            print('Нельзя изменить дату на дату из прошлого')
            return
        self.__created_at = new_date



if __name__ == '__main__':

    task = Task("Купить огурцы", "Купить огурцы для салата")
    print(task.name)
    print(task.description)
    print(task.status)
    print(task.created_at)

    task2 = Task.new_task('купить что-нибудь', 'купить всё равно что', 'Прямо сейчас')
    print(task2.name)
    print(task2.description)
    print(task2.status)
    print(task2.created_at)

    task2.created_at = '02.02.2025'
    task2.created_at = '29.05.2025'
    print(task2.created_at)

