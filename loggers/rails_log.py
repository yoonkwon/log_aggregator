import io

import maya
import sh


class RailsLog:
    logs = []

    def __init__(self, filepath, n=None, width=-1, _type=None, color="red"):
        if n is None or n < 0:
            res = sh.cat(filepath)
        else:
            res = sh.tail("-n", str(n), filepath)

        buf = io.StringIO(str(res))
        if _type is None:
            _type = type(self).__name__
        while True:
            line = buf.readline()
            if not line:
                break
            try:
                components = line.split(" ")
                timestamp = maya.parse(components[1][1:]+"+0900").datetime(to_timezone='Asia/Seoul')
                rest = (' '.join(components[7:])).strip()[:width]
                self.logs.append(dict(log_type=_type, ts=timestamp, msg=rest, color=color))
            except Exception:
                pass