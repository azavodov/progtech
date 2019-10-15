# coding=windows-1251
# Zavodov Andrey, P3410


# 1. Вх: список чисел, Возвр: список чисел, где повторяющиеся числа урезаны до одного
# пример [0, 2, 2, 3] returns [0, 2, 3].
def task_1_1(arr):
    return list({i: None for i in arr}.keys())


def task_1_2(arr):
    return list(set(arr))


# 2. Вх: Два списка упорядоченных по возрастанию,
# Возвр: новый отсортированный объединенный список
def task_2(arr1, arr2):
    return sorted(arr1 + arr2)


if __name__ == '__main__':
    print(task_1_1([0, 2, 2, 3, 4, 4, 4, 0, 4, 5]))
    print(task_1_2([0, 2, 2, 3, 4, 4, 4, 0, 4, 5]))
    print(task_2([1, 2, 4, 6], [1, 3, 5, 6, 3, 5, 1]))
