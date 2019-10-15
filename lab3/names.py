# coding=windows-1251
# Zavodov Andrey, P3410
import sys
from bs4 import BeautifulSoup


def extract_names(filename):
    """
    Вход: nameYYYY.html,
    Выход: список начинается с года, продолжается имя-ранг в алфавитном порядке.
    '2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' и т.д.
    """
    data = []
    with open(filename) as f:
        soup = BeautifulSoup(f, "html.parser")
        table = soup.find_all('table')[2]

        rows = table.find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]
            data.append([ele for ele in cols if ele])

    formatted_data = list()
    for row in data:
        if len(row) < 3:
            continue
        formatted_data.extend([f"{row[1]} {row[0]}", f"{row[2]} {row[0]}"])

    return [filename.split('/')[-1][4:8]] + sorted(formatted_data)


def find_top_20(arr: list):
    return sorted(arr, key=lambda x: int(x.split()[1]) if len(x.split()) == 2 else x)[:20]


def main():
    args = sys.argv[1:]
    if not args:
        print('use: [--file] file [file ...]')
        sys.exit(1)

    all_names = list()
    print("Parsed files:")
    for arg in args:
        names = extract_names(arg)
        all_names.append(names)
        print(', '.join(names))

    print("Top 20:")
    for names in all_names:
        print(f"{names[0]} - {' | '.join(find_top_20(names[1:]))}")


if __name__ == '__main__':
    main()
