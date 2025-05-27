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