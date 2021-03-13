import json


class MessageHandler:

    @staticmethod
    def create_msg(msg):
        msg = json.dumps(msg)
        return msg.encode('utf-8')

    @staticmethod
    def load_msg(data):
        data = data.decode("utf-8")
        try:
            data = json.loads(data)
        except json.decoder.JSONDecodeError:
            data = None
        return data
