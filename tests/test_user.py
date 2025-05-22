def test_user_init(first_user, second_user):
    assert first_user.username == 'Monster'
    assert first_user.email == 'mon@steel.com'
    assert len(first_user.tasks_list) == 4

    assert first_user.user_count == 2
    assert second_user.user_count == 2

    assert first_user.all_tasks_count == 6
    assert second_user.all_tasks_count == 6
