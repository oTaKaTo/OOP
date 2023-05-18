def delete_minus_prototype(set):
    del_set = []
    for i in range(len(set)):
        temp_set = []
        for j in range(len(set[i])):
            if set[i][j] > 0 :
                temp_set.append(set[i][j])
        del_set.append(temp_set)
    return del_set

def delete_minus(set):
    del_set = [[set[i][j] for j in range(len(set[i])) if set[i][j] > 0]for i in range(len(set))]

    return del_set

x = [[1, -3, 2], [-8, 5], [-1, -4, -3]]

print(len(x))
print(delete_minus(x))
