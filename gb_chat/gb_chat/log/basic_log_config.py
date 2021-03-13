import datetime
import inspect
import logging
import operator
import sys
from functools import wraps
from logging.handlers import RotatingFileHandler


format = logging.Formatter('%(asctime)s %(levelname)s %(module)s %(message)s')


# Создать обработчик, который выводит сообщения с уровнем CRITICAL в поток stderr
def get_crit_file_handler():
    crit_hand = logging.StreamHandler(sys.stderr)
    crit_hand.setLevel(logging.CRITICAL)
    crit_hand.setFormatter(format)
    return crit_hand


def get_app_file_handler(log_filename, logger):
    # # Создать обработчик, который выводит сообщения в файл
    # applog_hand = logging.FileHandler(f'{log_filename}.log')
    # applog_hand.setFormatter(format)

    # # Создать регистратор верхнего уровня с именем 'app'
    # app_log = logging.getLogger(f'{logger}')
    # app_log.setLevel(logging.INFO)
    # app_log.addHandler(applog_hand)
    # app_log.addHandler(get_crit_file_handler())
    path_to_logfile = './log_journals'
    app_log = logging.getLogger(f'{logger}')
    app_log.setLevel(logging.INFO)
    name_handler = RotatingFileHandler(f'{path_to_logfile}/{log_filename}.log', maxBytes=2000, backupCount=5)
    app_log.addHandler(name_handler)
    app_log.addHandler(get_crit_file_handler())

    return app_log


def log(func):

    time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    func_name = str(func)

    # возьми текущий фрейм объект (frame object)
    current_frame = inspect.currentframe()

    # получи фрейм объект, который его вызвал
    caller_frame = current_frame.f_back

    # возьми у вызвавшего фрейма исполняемый в нём объект типа "код" (code object)
    code_obj = caller_frame.f_code

    # и получи его имя
    code_obj_name = code_obj.co_name

    def create_result_string(time, func_name, instance, *args, **kwargs):
        result_string = f'{time} Функция {func_name} вызвана в {instance} с аргументами: {args} {kwargs}'
        return result_string

    @wraps(func)
    def call(*args, **kwargs):
        func_log = get_app_file_handler('func_log', 'called_functions')
        func_log.info(create_result_string(time, func_name, code_obj_name, args, kwargs))
        return func(*args, **kwargs)

    return call
