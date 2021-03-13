from basic_log_config import *
import datetime

today = datetime.datetime.now().strftime('%Y-%m-%d')
log_path = './log_journals/'

log_filename = log_path + 'server_journal ' + str(today)

get_app_file_handler(log_filename, 'server_journal')