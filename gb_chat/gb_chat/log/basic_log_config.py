import logging
import sys
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

    app_log = logging.getLogger(f'{logger}')
    app_log.setLevel(logging.INFO)
    name_handler = RotatingFileHandler(f'{log_filename}.log', maxBytes=2000, backupCount=5)
    app_log.addHandler(name_handler)
    app_log.addHandler(get_crit_file_handler())

    return app_log


# Изменить уровень важности для регистратора 'server_journal.net'
# logging.getLogger('server_journal.net').setLevel(logging.ERROR)
