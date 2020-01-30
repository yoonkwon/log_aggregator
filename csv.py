import os
import sys
from datetime import datetime

from dotenv import load_dotenv

from rails_log import RailsLog

if __name__ == '__main__':
    title = sys.argv[1] or 'trial'
    load_dotenv()
    logger = RailsLog(os.getenv("PERFORMANCE_LOG_PATH"), width=-1)
    path = os.getenv('PERFORMANCE_LOG_DEST_DIR')+"/{title}_performance{ts}.csv".format(
        title=title,
        ts=datetime.today().strftime("%Y%m%d%H%M%S%f"))
    with open(path, 'w') as f:
        for i, log in enumerate(logger.logs):
            if i > 0:
                f.write(os.linesep)
            f.write(log['msg'])
    print(len(logger.logs))

