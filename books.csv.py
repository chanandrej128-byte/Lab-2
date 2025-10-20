# Лабораторная работа №2 (Часть 1 — Работа с CSV-файлом)
#
# Автор: Чэнь Бохань
# Вариант: №8
#
# ⸻
#
# Задание
# 	1.	Вывести количество записей, у которых название книги длиннее 30 символов.
# 	2.	Реализовать поиск книг по автору.
# Ограничение варианта №8: только книги, изданные в 2015 и 2018 годах.
# 	3.	Сгенерировать 20 библиографических ссылок в формате
# «Автор. Название – Год»
# и сохранить результат в файл references.txt.

from csv import reader
def count_long_titles():

    flag2 = 0
    with open('books.csv', 'r', encoding='cp1251') as f:
        table = reader(f, delimiter=';')
        for row in table:
            title = row[1]
            if len(title) > 30:
                flag2 += 1
    print(f'Количество книг с длинным названием (>30 символов): {flag2}')

def search(table,search_line):
    flag=0
    output = open('result2.txt', "w", encoding="utf-8")

    for row in table:
        year = row[6].split()[0].split('.')[-1]
        if year not in ('2015', '2018'):
            continue

        else:
            if find_string(row[1],search_line)!=-1:
                flag+=1
                print(f"{row[0]}{row[1]}")
                output.write(f'{row[0]}. {row[1]} - {year}\n')


def generate_references():

    import random

    with open('books.csv', 'r', encoding='cp1251') as f:
        table = list(reader(f, delimiter=';'))
        books = table[1:]

    sample = random.sample(books, min(20, len(books)))


    with open('references.txt', 'w', encoding='utf-8') as out:
        for i, row in enumerate(sample, start=1):
            try:
                author = row[3]
                title = row[1]
                year=row[6].split()[0].split('.')[-1]
                out.write(f"{i}. {author}. {title} - {year}\n")
            except IndexError:
                continue

    print("✅ Файл references.txt создан (20 библиографических записей).")
    print("----- Содержимое файла -----")
    with open('references.txt', 'r', encoding='utf-8') as check:
        print(check.read())

def find_string(string,search_line):
    lower_case=string.lower()
    index=lower_case.find(search_line.lower())
    return index

while True:
    search_line =input("input book's name what you want:")
    if search_line in ['0','']:
        break

    try:
        with open('books.csv','r', encoding='cp1251', newline='')as csvfile:
            table =reader(csvfile,delimiter=';')
            search(table,search_line)
            count_long_titles()
            generate_references()



    except FileNotFoundError:
        print("not find site!")


