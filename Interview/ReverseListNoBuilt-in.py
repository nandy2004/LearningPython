def reverse_list(lst):
    n = len(lst)
    rev = [0] * n  # manually create same-size list
    for i in range(n):
        rev[i] = lst[n - i - 1]
    return rev
numbers = [1, 2, 3, 4, 5]
print(reverse_list(numbers))