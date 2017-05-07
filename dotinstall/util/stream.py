def streamToString(stream):
    ret = ""
    if stream is not None:
        for line in stream:
            ret += line.decode("utf-8")
    return ret
