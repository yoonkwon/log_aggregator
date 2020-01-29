import os

from termcolor import colored
import sys
from mysql_log import MysqlLog
from rails_log import RailsLog
from dotenv import load_dotenv

if __name__ == '__main__':
    N = int(sys.argv[1] or 100)
    load_dotenv()
    mysql = MysqlLog(os.getenv("MYSQL_LOG_PATH"), int(N*2))
    trades = RailsLog(os.getenv("TRADES_LOG_PATH"), N)

    logs = sorted(mysql.logs + trades.logs, key=lambda k: k['ts'])

    for i, log in enumerate(logs):
        color = 'blue'
        if log['log_type'] == RailsLog.__name__:
            color = 'red'
        print(colored(' '.join([str(i), log['ts'].strftime('%Y-%m-%d %H:%M:%S.%f')[:-3], log['msg']]), color))
