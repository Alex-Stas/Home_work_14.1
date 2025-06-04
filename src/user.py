from src.task import Task

class User:
    username: str
    email: str
    first_name: str
    last_name: str
    task_list: list
    user_count = 0
    all_tasks_count = 0

    def __init__(self, username, email, first_name, last_name, task_list=None):
        self.username = username
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.__task_list = task_list if task_list else []
        User.user_count += 1
        User.all_tasks_count += len(task_list) if task_list else 0

    def __str__(self):
        return f'{self.last_name} {self.first_name}, E-mail: {self.email} , Всего задач в списке: {len(self.__task_list)}'

    def __iter__(self):
        self._current_task = 0  # Сбрасываем индекс при начале новой итерации
        return self

    def __next__(self):
        if self._current_task < len(self.task_in_list):
            task = self.task_in_list[self._current_task]
            self._current_task += 1
            return task
        else:
            raise StopIteration


    @property
    def task_list(self):
        task_str = ''
        for task in self.__task_list:
            task_str += f'{str(task)}\n'
        return task_str

    @task_list.setter
    def task_list(self, task: Task):
        if isinstance(task, Task):
            self.__task_list.append(task)
            User.all_tasks_count += 1
        else:
            raise TypeError

    @property
    def task_in_list(self):
        return self.__task_list



if __name__ == '__main__':

    task1 = Task("Купить огурцы", "Купить огурцы для салата")
    task2 = Task("Купить помидоры", "Купить помидоры для салата")
    task3 = Task("Купить лук", "Купить лук для салата")
    task4 = Task("Купить перец", "Купить перец для салата")

    user = User('Monster', 'mon@steel.com', 'Michael', 'Ontario', [task1, task2, task3, task4])


    print(user.username)
    print(user.email)
    print(user.first_name)
    print(user.last_name)
    print(user.task_list)

    print(user.user_count)
    print(User.all_tasks_count)

    task5 = Task("Купить twitter", "Купить twitter у Маска")

    user.task_list = task5

    print(user.task_list)
    print(User.all_tasks_count)

    print(user)
    print()

    for i in user:
        print(i)
