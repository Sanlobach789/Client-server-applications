import datetime
import inspect
from functools import wraps

from gb_chat.gb_chat.log.basic_log_config import log


@log
def foo(a, b):
    return print(a + b)


foo(2, 5)
