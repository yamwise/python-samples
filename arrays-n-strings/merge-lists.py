def mergeLists(list1, list2):
    result = []
    i = 0
    j = 0
    while i < len(list1) or j < len(list2):
        if list1[i] < list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1
    return result


my_list = [3, 4, 6, 10, 11, 15]
alices_list = [1, 5, 8, 12, 14, 19]

print(mergeLists(my_list, alices_list))
