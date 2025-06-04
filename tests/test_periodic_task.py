import pytest

def test_task_init(periodic_task1):

    assert periodic_task1.name == "Купить огурцы"
    assert periodic_task1.description == "Купить огурцы для салата"
    assert periodic_task1.status == 'Ожидает старта'
    assert periodic_task1.created_at =='01.01.2025'
    assert periodic_task1.start_date == '01.06.2025'
    assert periodic_task1.end_date == '10.06.2025'
    assert periodic_task1.frequency == 'Ежедневно'
    assert periodic_task1.run_time == 60

def test_periodic_task_add(periodic_task1, periodic_task2):
    assert periodic_task1 + periodic_task2 == 120

def test_periodic_task_add_error(periodic_task1, periodic_task2):
    with pytest.raises(TypeError):
        result = periodic_task1 + 1
