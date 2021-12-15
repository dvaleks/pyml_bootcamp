'''
Задание:
Написать программу, которая выполняет следующее:

1) вычисляет значения функций f1(x) = x/(x+100) и f2(x) = 1/x при изме-
нении x в диапазоне от 5 до 90 с шагом 1.

2) вычисляет значение функций f3(x) = 20*(f1(x) + f2(x))/x.
3) представляет результат в виде словаря следующего вида*: {x1: [f1(x1),
f2(x1), f3(x1)], x2: [f1(x2), f2(x2), f3(x2)], ...};
4) сохраняет результат вычислений в CSV-файл, заголовком (столбцами)
которого являются значения x, f1(x), f2(x), f3(x);
5) читает записанный CSV-файл и представляет результат в виде списка
[[x1, f1(x1), f2(x1), f3(x1)], [x2, f1(x2), f2(x2), f3(x2)], ...];
6) сохраняет список [[x1, f1(x1), f2(x1), f3(x1)], [x2, f1(x2), f2(x2), f3(x2)], ...] в
JSON-файл.
*Примечание: вычисление значений f1(x), f2(x), f3(x) реализовать в виде

отдельных Python функций (можно с применением лямбда-выражений). Из-
менение x в диапазоне от 5 до 90 с шагом 1 реализовать в виде генератора.
'''

import csv
import json
import os


def f1(x):
    return x / (x + 100)


def f2(x):
    return 1 / x


def f3(x):
    return 20 * (f1(x) + f2(x)) / x


def main():

    def generator_row(start, end):
        for i in range(start, end):
            yield {'x': i, 'f1(x)': f1(i), 'f2(x)': f2(i), 'f3(x)': f3(i)}

    filepath = os.path.join(os.getcwd(), 'output.csv')
    with open(filepath, 'w') as file:
        writer = csv.DictWriter(file, fieldnames=['x', 'f1(x)', 'f2(x)', 'f3(x)'])
        writer.writeheader()
        for row in generator_row(5, 91):
            writer.writerow(row)
    print('Write file: output.csv')

    with open(filepath, 'r') as file:
        csv_file = csv.DictReader(file)
        arr2d = [list(row.values()) for row in csv_file]

    filepath = os.path.join(os.getcwd(), 'output.json')
    with open(filepath, 'w') as file:
        json.dump(arr2d, file)
    print('Write file: output.json')


if __name__ == '__main__':
    main()
