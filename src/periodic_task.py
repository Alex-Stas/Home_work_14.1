from src.task import Task

class PeriodicTask(Task):
    def __init__(self, name, description, start_date, end_date, status='Ожидает старта', created_at=None, run_time=0, frequency='Ежедневно'):
        super().__init__(name, description, status, created_at, run_time)
        self.start_date = start_date
        self.end_date = end_date
        self.frequency = frequency

    def __add__(self, other):
        if type(other) is PeriodicTask:
            return self.run_time + other.run_time
        raise TypeError

if __name__ == '__main__':

    periodic_task = PeriodicTask("Купить огурцы", "Купить огурцы для салата", '01.06.2025', '10.06.2025', run_time=60)
    print(periodic_task.name)
    print(periodic_task.description)
    print(periodic_task.status)
    print(periodic_task.created_at)
    print(periodic_task.run_time)

    print(periodic_task.start_date)
    print(periodic_task.end_date)
    print(periodic_task.frequency)

    periodic_task2 = PeriodicTask("Купить огурцы", "Купить огурцы для салата", '01.06.2025', '10.06.2025', run_time=60)
    task = Task('купить что-нибудь', 'купить всё равно что', 'Прямо сейчас')

    print(periodic_task + periodic_task2)
    print(periodic_task + task)

    # task2 = Task.new_task('купить что-нибудь', 'купить всё равно что', 'Прямо сейчас')
    # print(task2.name)
    # print(task2.description)
    # print(task2.status)
    # print(task2.created_at)
    #
    # task2.created_at = '02.02.2025'
    # task2.created_at = '01.06.2025'
    # print(task2.created_at)
    #
    # print(task + task2)

