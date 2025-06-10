import pytest
from src.task import Task

def test_user_init(first_user, second_user):

    assert first_user.username == 'Monster'
    assert first_user.email == 'mon@steel.com'
    assert len(first_user.task_in_list) == 4

    assert first_user.user_count == 2
    assert second_user.user_count == 2

    assert first_user.all_tasks_count == 6
    assert second_user.all_tasks_count == 6


def test_user_task_list_property (second_user):
    assert second_user.task_list == ('Убить президента, Статус выполнения: Ожидает старта, Дата создания: 27.05.2025\n'
                                     'Устроить переворот, Статус выполнения: Ожидает старта, Дата создания: 27.05.2025\n')

def test_user_task_list_setter (second_user, task):
    assert len(second_user.task_in_list) == 2
    second_user.task_list = task
    assert len(second_user.task_in_list) == 3


def test_user_str(first_user):
    assert str(first_user) == 'Ontario Michael, E-mail: mon@steel.com , Всего задач в списке: 4'


def test_task_iterator(task_iterator):
    iter(task_iterator) # перезапуск итератора для гарантии сброса индекса
    assert task_iterator.index == 0
    assert next(task_iterator).name == "Убить президента"
    assert next(task_iterator).name == "Устроить переворот"
    with pytest.raises(StopIteration):
        next(task_iterator)

def test_user_task_list_setter_error (second_user):
    with pytest.raises(TypeError):
        second_user.task_list = 1

def test_user_task_list_setter_periodic_deadline (second_user, periodic_task2, deadline_task1):
    assert len(second_user.task_in_list) == 2
    second_user.task_list = periodic_task2
    assert len(second_user.task_in_list) == 3
    assert second_user.task_in_list[-1].name == 'Купить помидоры'
    second_user.task_list = deadline_task1
    assert len(second_user.task_in_list) == 4
    assert second_user.task_in_list[-1].name == 'Купить огурцы'

def test_average_runtime(first_user, user_without_tasks):
    assert first_user.average_task_runtime() == 20
    assert user_without_tasks.average_task_runtime() == 0

def test_custom_exception(capsys, first_user):
    assert len(first_user.task_in_list) == 4

    task_add = Task("Убить президента", "Убить президента, которого выберут", created_at='27.05.2025')
    first_user.task_list = task_add
    message = capsys.readouterr()
    assert message.out.strip().split('\n')[-2] == "Нельзя задать задачу с нулевым временем выполнения"
    assert message.out.strip().split('\n')[-1] == "Обработка добавления задачи завершена"

    task_add2 = Task("Убить президента", "Убить президента, которого выберут", created_at='27.05.2025', run_time=30)
    first_user.task_list = task_add2
    message = capsys.readouterr()
    assert message.out.strip().split('\n')[-2] == "Задача добавлена успешно"
    assert message.out.strip().split('\n')[-1] == "Обработка добавления задачи завершена"
