import pytest

from src.user import User
from src.task import Task

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
            Task("Убить президента", "Убить президента, которого выберут"),
            Task("Устроить переворот", "Устроить переворот в Сомали")
        ]
    )


@pytest.fixture
def task():
    return Task("Купить огурцы", "Купить огурцы для салата", created_at='01.01.2025')