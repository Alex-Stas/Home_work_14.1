import pytest

def test_task_init(deadline_task1):

    assert deadline_task1.name == "Купить огурцы"
    assert deadline_task1.description == "Купить огурцы для салата"
    assert deadline_task1.status == 'Ожидает старта'
    assert deadline_task1.created_at =='01.01.2025'
    assert deadline_task1.deadline == '20.06.2025'
    assert deadline_task1.run_time == 60

def test_deadline_task_add(deadline_task1, deadline_task2):
    assert deadline_task1 + deadline_task2 == 120

def test_periodic_task_add_error(deadline_task1, deadline_task2):
    with pytest.raises(TypeError):
        result = deadline_task1 + 1