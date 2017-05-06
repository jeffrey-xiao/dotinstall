def streamToString (stream):
    ret = ""
    if stream != None:
        for line in stream:
            ret += line
    return ret
