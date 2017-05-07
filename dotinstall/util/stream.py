def streamToString(stream):
    ret = ""
    if stream is not None:
        for line in stream:
            ret += line
    return ret
