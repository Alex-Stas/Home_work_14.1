import json
import os

from src.task import Task
from src.user import User

def read_json(path: str) -> dict:
    full_path = os.path.abspath(path)
    with open(full_path, 'r', encoding='UTF-8') as file:
        data = json.load(file)
    return data

def create_objects_fm_json(data):
    users = []
    for user in data:
        tasks = []
        for task in user['task_list']:
            tasks.append(Task(**task))
        user['task_list'] = tasks
        users.append(User(**user))
    return users


if __name__ == '__main__':
    raw_data = read_json('../data/user_data.json')
    users_data = create_objects_fm_json(raw_data)

    print(raw_data)

    for user in users_data:
        print(user.username)
        print(user.email)
        print(user.first_name)
        print(user.last_name)
        print(user.task_list)

    # print(users_data)
