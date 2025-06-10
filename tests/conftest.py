import pytest

from src.user import User
from src.task import Task
from src.task_iteration import TaskIterator
from src.periodic_task import PeriodicTask
from src.deadline_task import DeadlineTask


@pytest.fixture
def first_user():
    return User(
        username='Monster',
        email='mon@steel.com',
        first_name='Michael',
        last_name='Ontario',
        task_list=[
            Task("Купить огурцы", "Купить огурцы для салата", run_time=10),
            Task("Купить помидоры", "Купить помидоры для салата", run_time=10),
            Task("Купить лук", "Купить лук для салата", run_time=30),
            Task("Купить перец", "Купить перец для салата", run_time=30)
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
    return Task("Купить огурцы", "Купить огурцы для салата", created_at='01.01.2025', run_time=25)

@pytest.fixture
def task_with_run_time1():
    return Task("Купить Боинг>", "Купить Боинг для перелета", created_at='01.01.2025', run_time=2000)

@pytest.fixture
def task_with_run_time2():
    return Task("Купить Аирбас>", "Купить Аирбас для перелета", created_at='01.01.2025', run_time=2500)

@pytest.fixture
def task_iterator(second_user):
    return TaskIterator(second_user)

@pytest.fixture
def periodic_task1():
    return PeriodicTask("Купить огурцы", "Купить огурцы для салата", '01.06.2025', '10.06.2025', created_at='01.01.2025', run_time=60)

@pytest.fixture
def periodic_task2():
    return PeriodicTask("Купить помидоры", "Купить помидоры для закуски", '01.06.2025', '10.06.2025', created_at='01.01.2025', run_time=60)

@pytest.fixture
def deadline_task1():
    return DeadlineTask("Купить огурцы", "Купить огурцы для салата", '20.06.2025', created_at='01.01.2025', run_time=60)

@pytest.fixture
def deadline_task2():
    return DeadlineTask("Купить помидоры", "Купить помидоры для закуски", '20.06.2025',  created_at='01.01.2025', run_time=60)

@pytest.fixture
def user_without_tasks():
    return User(
        username='Monsteino',
        email='monst@steel.com',
        first_name='Moor',
        last_name='Rodger'
    )