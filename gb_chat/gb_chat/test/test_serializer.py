import json

from gb_chat.messages import Authenticate
from gb_chat.serializer import Serializer


def test_serialize_authenticate():
    msg = Authenticate("DmitryErlikh", "MySuperPassword")

    expected_time = 123
    expected_msg = {
        "action": "authenticate",
        "time": expected_time,
        "user": {"account_name": msg.account_name, "password": msg.password,},
    }
    expected_data = json.dumps(expected_msg).encode("utf-8")

    sut = Serializer(get_time_fn=lambda: expected_time)
    assert sut.serialize(msg) == expected_data
