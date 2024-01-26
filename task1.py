'''
Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
В результирующем списке не должно быть дубликатов.
'''

input_list = [1, 1, 2, 3, 3, 4, 5, 5, 6, 6, 7, 7, 7, 8, 9, 9, 9, 9]


def return_duplicates(input_list):
    result = []
    for item in input_list:
        if input_list.count(item) > 1 and item not in result:
            result.append(item)
    return result


print(return_duplicates(input_list))
