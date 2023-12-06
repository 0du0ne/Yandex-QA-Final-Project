# Панна Илья 11-ая когорта - Финальный проект. Инженер по тестированию плюс

import sender_stand_request


def get_track_number():
    response = sender_stand_request.post_new_order()
    return response.json()["track"]


def test_get_order_track():
    track_number = get_track_number()
    get_response = sender_stand_request.get_order_track(track_number)
    assert get_response.status_code == 200