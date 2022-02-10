"""
Написать программу, которая обладает следующими функциональными
возможностями:
1. Объединяет два Pandas датафрейма (df1 и df2) по двум столбцам (x_1,
y_1 и x_2, y_2), так чтобы остались только:
 общие строки – создает df3 (предусмотреть наличие аргументов
left_on и right_on для индексов «левого» и «правого» датафремов);
 остались все строки – создает df4.
2. Находит в датафрейме df4 позиции всех отсутствующих значений

(формирует список из «координат» таких значений) и заменяет их значени-
ем 0.

3. Добавляет к датафрейму df4 столбец z_avg справа, в котором вычисля-
ется арифметическое среднее (z_left + z_right)/2.
"""

import pandas as pd
import numpy as np

df1 = pd.DataFrame({'x_1': ['A', 'B', 'C'] * 3,
                    'y_1': ['D', 'E', 'F'] * 3,
                    'z': np.random.randint(0, 20, 9)})
df2 = pd.DataFrame({'x_2': ['A', 'B', 'C'] * 4,
                    'y_2': ['D', 'E'] * 6,
                    'z': np.random.randint(0, 20, 12)})

df3 = pd.merge(df1, df2, how='inner',
               left_on=['x_1', 'y_1'], right_on=['x_2', 'y_2'],
               suffixes=('_left', '_right'))

df4 = pd.merge(df1, df2, how='outer',
               left_on=['x_1', 'y_1'], right_on=['x_2', 'y_2'],
               suffixes=('_left', '_right'))

# https://stackoverflow.com/questions/54905677/python-get-coordinate-with-pair-of-nans
df4_nan_coords = [[r, df4.columns[c]] for r, c in np.argwhere(pd.isnull(df4).values)]

df4.fillna(0, inplace=True)
df4['z_avg'] = (df4['z_left'] + df4['z_right'] ) / 2
print(df4)
