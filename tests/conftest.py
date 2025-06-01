import pytest

from src.user import User
from src.task import Task
from src.task_iteration import TaskIterator


@pytest.fixture
def first_user():
    return User(
        username='Monster',
        email='mon@steel.com',
        first_name='Michael',
        last_name='Ontario',
        task_list=[
            Task("Купить огурцы", "Купить огурцы для салата"),
            Task("Купить помидоры", "Купить помидоры для салата"),
            Task("Купить лук", "Купить лук для салата"),
            Task("Купить перец", "Купить перец для салата")
        ]
    )


@pytest.fixture
def second_user():
    return User(
        username='Crash',
        email='over@steel.com',
        first_name='Crash',
        last_name='Override',
        task_list=[
            Task("Убить президента", "Убить президента, которого выберут", created_at='27.05.2025'),
            Task("Устроить переворот", "Устроить переворот в Сомали", created_at='27.05.2025')
        ]
    )




@pytest.fixture
def task():
    return Task("Купить огурцы", "Купить огурцы для салата", created_at='01.01.2025')

@pytest.fixture
def task_with_run_time1():
    return Task("Купить Боинг>", "Купить Боинг для перелета", created_at='01.01.2025', run_time=2000)

@pytest.fixture
def task_with_run_time2():
    return Task("Купить Аирбас>", "Купить Аирбас для перелета", created_at='01.01.2025', run_time=2500)

@pytest.fixture
def task_iterator(second_user):
    return TaskIterator(second_user)

