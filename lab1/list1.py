# coding=windows-1251
# Zavodov Andrey, P3410


# 1.
# Вх: список строк, Возвр: кол-во строк
# где строка > 2 символов и первый символ == последнему
def task_1(words: list):
    return len([word for word in words if len(word) > 2 and word[0] == word[-1]])


# 2. 
# Вх: список строк, Возвр: список со строками (упорядочено)
# за искл всех строк начинающихся с 'x', которые попадают в начало списка.
# ['tix', 'xyz', 'apple', 'xacadu', 'aabbbccc'] -> ['xacadu', 'xyz', 'aabbbccc', 'apple', 'tix']
def task_2(words: list):
    return sorted([w for w in words if len(w[0]) and w[0] == 'x']) + \
           sorted([w for w in words if len(w[0]) and w[0] != 'x'])


# 3. 
# Вх: список непустых кортежей, 
# Возвр: список сортир по возрастанию последнего элемента в каждом корт.
# [(1, 7), (1, 3), (3, 4, 5), (2, 2)] -> [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
def task_3(cort: list):
    return sorted(cort, key=lambda x: x[-1] if len(x) else None)


if __name__ == '__main__':
    print(task_1(['ww', 'www', 'word3', 'word4w']))
    print(task_2(['tix', 'xyz', 'apple', 'xacadu', 'aabbbccc']))
    print(task_3([(1, 7), (1, 3), (3, 4, 5), (2, 2)]))
