import io

import maya
import sh
from pendulum.parsing import ParserError


class MysqlLog:
    logs = []

    def __init__(self, filepath, n=1000):
        res = sh.contrib.sudo.tail("-n", str(n), filepath)
        buf = io.StringIO(str(res))
        while True:
            line = buf.readline()
            if not line:
                break
            components = line.split(" ")
            try:
                timestamp = maya.parse(components[0]).datetime(to_timezone='Asia/Seoul')
                rest = (' '.join(components[1:])).strip()[:80]
                self.logs.append(dict(log_type=type(self).__name__, ts=timestamp, msg=rest))
            except ParserError:
                pass
            except ValueError:
                pass
