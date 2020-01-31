import os

from termcolor import colored
import sys
from loggers.mysql_log import MysqlLog
from loggers.rails_log import RailsLog
from dotenv import load_dotenv

if __name__ == '__main__':
    N = int(sys.argv[1]) if len(sys.argv) > 1 else -1
    load_dotenv()
    mysql = MysqlLog(os.getenv("MYSQL_LOG_PATH"), N, width=80)
    trades = RailsLog(os.getenv("TRADES_LOG_PATH"), N, width=80)

    logs = sorted(mysql.logs + trades.logs, key=lambda k: k['ts'])

    for i, log in enumerate(logs):
        print(colored(' '.join([str(i), log['ts'].strftime('%Y-%m-%d %H:%M:%S.%f')[:-3], log['msg']]), log['color']))
