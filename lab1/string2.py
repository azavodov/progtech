# coding=windows-1251
# Zavodov Andrey, P3410


# 1.
# Вх: строка. Если длина > 3, добавить в конец "ing", если в конце нет уже "ing", иначе добавить "ly".
import re


def task_1(s):
    return f'{s}ing' if len(s) > 3 and not s.endswith('ing') else f'{s}ly'


# 2. 
# Вх: строка. Заменить подстроку от 'not' до 'bad'. ('bad' после 'not') на 'good'.
# Пример: So 'This music is not so bad!' -> This music is good!
def task_2(s):
    return re.sub(r'not.*bad', 'good', s)


if __name__ == '__main__':
    print(f"ing -> {task_1('ing')}")
    print(f"string -> {task_1('string')}")
    print(f"strings -> {task_1('strings')}")
    print(f"This music is not so bad! -> {task_2('This music is not so bad!')}")
