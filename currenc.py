# Лабораторная работа №2 (Часть 2 — Работа с XML-файлом)
#
# Автор: Чэнь Бохань
# Вариант: №8
#
#  Задание
# 	1.	Распарсить файл currency.xml.
# 	2.	Извлечь данные о валюте: теги <CharCode> и <Nominal>.
# 	3.	Создать словарь вида «CharCode – Nominal».
# 	4.	Сохранить результат в файл currency_result.txt.
#
import xml.etree.ElementTree as ET

tree = ET.parse('currency.xml')
root = tree.getroot()

result = {}
for v in root.findall('.//Valute'):
    char = (v.findtext('CharCode') or '').strip()
    nom  = (v.findtext('Nominal')  or '').strip()
    if char and nom:
        result[char] = int(nom)

with open('currency_result.txt', 'w', encoding='utf-8') as f:
    for k, v in result.items():
        f.write(f'{k}: {v}\n')


print('✅ currency_result.txt has been made')
