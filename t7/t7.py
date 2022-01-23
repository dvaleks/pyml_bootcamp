import numpy as np
from typing import Tuple


class DataProcessor:
    supported_ops = {
        'abs': np.abs,
        'fabs': np.fabs,
        'sqrt': np.sqrt,
        'square': np.square,
        'exp': np.exp,
        'log': np.log,
        'log10': np.log10,
        'sign': np.sign,
        'ceil': np.ceil,
        'floor': np.floor,
        'rint': np.rint,
        'modf': np.modf,
        'isnan': np.isnan,
        'isfinite': np.isfinite,
        'isinf': np.isinf,
        'logical_not': np.logical_not
    }

    def __init__(self, arr):
        self.arr = arr
        self.n_rows, self.n_columns = self.arr.shape

    def _parse_slice_indexes(self, row_indexes, col_indexes):
        if row_indexes is None:
            row_indexes = (0, self.n_rows)
        if col_indexes is None:
            col_indexes = (0, self.n_columns)
        return row_indexes, col_indexes

    def slice_op(self, operation_name: str,
                 row_indexes: Tuple[int, int] = None, col_indexes: Tuple[int, int] = None) -> np.array:
        if operation_name not in self.supported_ops:
            raise ValueError('Unsupported operation: {0}'.format(operation_name))
        row_indexes, col_indexes = self._parse_slice_indexes(row_indexes, col_indexes)
        z = np.zeros_like(self.arr)
        op = self.supported_ops[operation_name]
        z[row_indexes[0]:row_indexes[1], col_indexes[0]:col_indexes[1]] = \
            op(self.arr[row_indexes[0]:row_indexes[1], col_indexes[0]:col_indexes[1]])
        return z


data = np.random.randn(4, 7)
print('data:')
print(data)
print('-' * 10)

dp = DataProcessor(data)
data2 = dp.slice_op('abs', (1, 3), (1, 3))
print('data2:')
print(data2)

for op in DataProcessor.supported_ops:
    try:
        print('doing op:', op, end='')
        dp.slice_op(op)
    except Exception as ex:
        print(' - exception: {0}'.format(ex))
    else:
        print(' - OK')

print('-' * 100)
print('Transform 2d array to 3d')
print('-' * 100)


def transform_2d_to_3d(inp, n):
    data = np.reshape(inp, (1, inp.shape[0], inp.shape[1]))
    layer = data.copy()
    for i in range(n):
        data = np.append(data, layer, axis=0)
    return data


data = np.random.randn(2, 3)
print('input 2d array:')
print(data)
print('-' * 100)
print('transform_2d_to_3d(data, 3)')
print('output 3d array:')
print(transform_2d_to_3d(data, 3))
