import pytest
from src.task import Task
from src.periodic_task import PeriodicTask
from src.deadline_task import DeadlineTask

def test_print_mixin_task(capsys):
    Task("Купить огурцы", "Купить огурцы для салата", created_at='01.01.2025')
    message = capsys.readouterr()
    assert message.out.strip() == 'Task (Купить огурцы, Купить огурцы для салата, Ожидает старта, 01.01.2025)'

    PeriodicTask("Купить огурцы", "Купить огурцы для салата", '01.06.2025', '10.06.2025', created_at='01.01.2025', run_time=60)
    message = capsys.readouterr()
    assert message.out.strip() == 'PeriodicTask (Купить огурцы, Купить огурцы для салата, Ожидает старта, 01.01.2025)'

    DeadlineTask("Купить огурцы", "Купить огурцы для салата", '20.06.2025', created_at='01.01.2025', run_time=60)
    message = capsys.readouterr()
    assert message.out.strip() == 'DeadlineTask (Купить огурцы, Купить огурцы для салата, Ожидает старта, 01.01.2025)'
