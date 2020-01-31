import os

from termcolor import colored
import sys
from loggers.rails_log import RailsLog
from dotenv import load_dotenv

if __name__ == '__main__':
    N = int(sys.argv[1]) if len(sys.argv) > 1 else -1
    load_dotenv()
    rails1 = RailsLog(os.getenv("RAILS_LOG_FILE1"), N, _type="Rails1")
    rails2 = RailsLog(os.getenv("RAILS_LOG_FILE2"), N, _type="Rails2", color="white")

    logs = sorted(rails1.logs + rails2.logs, key=lambda k: k['ts'])

    for i, log in enumerate(logs):
        print(colored(' '.join([str(i), log['ts'].strftime('%Y-%m-%d %H:%M:%S.%f')[:-3], log['msg']]), log['color']))
