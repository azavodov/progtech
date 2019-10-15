# coding=windows-1251
# Zavodov Andrey, P3410


# 1. 
# Входящие параметры: int <count> , 
# Результат: string в форме "Number of: <count>", где <count> число из вход.парам.
# Если число равно 10 или более, напечатать "many" вместо <count>
# Пример: (5) -> "Number of: 5"; (23) -> 'Number of: many'
def task_1(count: int) -> str:
    return f"Number of: {count if count < 10 else 'many'}"


# 2. 
# Входящие параметры: string s, 
# Результат: string из 2х первых и 2х последних символов s
# Пример 'welcome' -> 'weme'.
def task_2(s: str) -> str:
    return s[:2] + s[-2:] if len(s) > 3 else None


# 3. 
# Входящие параметры: string s,
# Результат: string где все вхождения 1го символа заменяются на '*' (кроме самого 1го символа)
# Пример: 'bibble' -> 'bi**le'; s.replace(stra, strb)
def task_3_1(s: str) -> str:
    return s[0] + ''.join([i if i != s[0] else '*' for i in s[1:]]) if len(s) > 1 else s


def task_3_2(s: str) -> str:
    return s[0] + s[1:].replace(s[0], '*') if len(s) > 1 else s


# 4
# Входящие параметры: string a и b, 
# Результат: string где <a> и <b> разделены пробелом, а превые 2 симв обоих строк заменены друг на друга
# Т.е. 'max', pid' -> 'pix mad'; 'dog', 'dinner' -> 'dig donner'
def task_4(a: str, b: str) -> str:
    return F"{b[:2]}{a[2:]} {a[:2]}{b[2:]}" if len(a) > 2 and len(b) > 2 else None


if __name__ == '__main__':
    print(task_1(9))
    print(task_1(10))

    print(task_2('welcome'))

    print(task_3_1('bibble'))
    print(task_3_2('bibble'))

    print(task_4('dog', 'dinner'))
