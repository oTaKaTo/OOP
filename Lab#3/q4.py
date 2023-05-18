def char_count(str):
    result = dict()
    for w in str:
        result[w] = str.count(w)
    return result