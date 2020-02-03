import hashlib
import time


def hump(value):
    assert isinstance(value, str)
    return value[0].upper()+ value[1:]

def genMd5(string):
    if string is None:
        return ""
    assert isinstance(string, str)
    m = hashlib.md5()
    m.update(string.encode('utf-8'))
    return m.hexdigest()

def timestamp():
    return int(round(time.time() * 1000))





