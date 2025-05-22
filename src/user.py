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
        self.task_list = task_list if task_list else []
        User.user_count += 1
        User.all_tasks_count += len(task_list) if task_list else 0


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