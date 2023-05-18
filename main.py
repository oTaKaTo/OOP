def merge_sort(list):
    if len(list) <= 1:
        return list

    middle = len(list) // 2
    left = list[:middle]
    right = list[middle:]

    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)


def merge(left, right):
    # write your code here
    list = (len(left) + len(right)) * [0]
    i = j = k = 0  # index of left, right, merged
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            list[k] = left[i]
            i += 1
        else:
            list[k] = right[j]
            j += 1
        k += 1  # move to next slot

    while i < len(left):
        list[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        list[k] = right[j]
        j += 1
        k += 1
    return list

test1 = [13, 22, 46, 89]
test2 = [4, 37, 58, 61]
print(merge(test1, test2))

test4 = [89, 61, 58, 46, 37, 22, 13, 4]
print(merge_sort(test4))

test3 = [89, 22, 46, 13, 37, 58, 61, 4]
print(merge_sort(test3))