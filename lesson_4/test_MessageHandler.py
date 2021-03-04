
from handler import MessageHandler
import unittest


msg = {
        "action": "test",
        "time": "test",
    }

data = b'{"action": "test", "time": "test"}'


class TestMessageHandler(unittest.TestCase):

    def test_create_msg(self):
        self.assertEqual(MessageHandler.create_msg(msg), data)

    def test_load_msg(self):
        self.assertEqual(MessageHandler.load_msg(data), msg)


if __name__ == "__main__":
    unittest.main()