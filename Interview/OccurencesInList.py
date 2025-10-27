def remove_all(lst, element):
    result = []
    for i in lst:
        if i != element:
            result.append(i)
    return result

numbers = [1, 2, 3, 2, 4, 2, 5]
print(remove_all(numbers, 2))