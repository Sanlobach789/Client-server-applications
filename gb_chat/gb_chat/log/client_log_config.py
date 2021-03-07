import logging
import sys

# Определить формат сообщений
format = logging.Formatter('%(asctime)s %(levelname)s %(module)s %(message)s')

# Создать обработчик, который выводит сообщения с уровнем CRITICAL в поток stderr
crit_hand = logging.StreamHandler(sys.stderr)
crit_hand.setLevel(logging.CRITICAL)
crit_hand.setFormatter(format)

# Создать обработчик, который выводит сообщения в файл
applog_hand = logging.FileHandler('client_journal.log')
applog_hand.setFormatter(format)

# Создать регистратор верхнего уровня с именем 'app'
app_log = logging.getLogger('client_journal')
app_log.setLevel(logging.INFO)
app_log.addHandler(applog_hand)
app_log.addHandler(crit_hand)

# Изменить уровень важности для регистратора 'client_journal.net'
# logging.getLogger('client_journal.net').setLevel(logging.ERROR)
