import io

import maya
import sh


class RailsLog:
    logs = []

    def __init__(self, filepath, n=None, width=80):
        if n is not None:
            res = sh.tail("-n", str(n), filepath)
        else:
            res = sh.cat(filepath)
        buf = io.StringIO(str(res))
        while True:
            line = buf.readline()
            if not line:
                break
            components = line.split(" ")
            timestamp = maya.parse(components[1][1:]+"+0900").datetime(to_timezone='Asia/Seoul')
            rest = (' '.join(components[7:])).strip()[:width]
            self.logs.append(dict(log_type=type(self).__name__, ts=timestamp, msg=rest))
