def is_plusone_dictionary(d):
    temp = list(d.keys())[0] - 1
    for x in d.keys():
        if x - temp != 1 or d[x] - x != 1:
            return False
        temp = d[x]
    return True

