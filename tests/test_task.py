import datetime
from src.task import Task

def test_task_init(task):

    assert task.name == "Купить огурцы"
    assert task.description == "Купить огурцы для салата"
    assert task.status == 'Ожидает старта'
    assert task.created_at =='01.01.2025'

def test_task_create ():
    task = Task("Купить огурцы", "Купить огурцы для салата")
    assert task.name == "Купить огурцы"
    assert task.description == "Купить огурцы для салата"
    assert task.status == 'Ожидает старта'
    assert task.created_at == datetime.datetime.now().date().strftime('%d.%m.%Y')

def test_task_update(capsys,task):
    assert task.created_at == '01.01.2025'
    past_date = datetime.datetime.now() - datetime.timedelta(days=1)
    task.created_at = past_date.date().strftime('%d.%m.%Y')
    message = capsys.readouterr()
    assert message.out.strip() == 'Нельзя изменить дату на дату из прошлого'
    task.created_at = datetime.datetime.now().date().strftime('%d.%m.%Y')
    assert task.created_at == datetime.datetime.now().date().strftime('%d.%m.%Y')


def test_task_str(task):
    assert str(task) == 'Купить огурцы, Статус выполнения: Ожидает старта, Дата создания: 01.01.2025'

def test_task_add(task_with_run_time1, task_with_run_time2):
    assert task_with_run_time1 + task_with_run_time2 == 4500




