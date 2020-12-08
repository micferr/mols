from typing import List

from structures.square import Square

def _generate_transversals(square: Square):
    """Generates all possible transversals for the given square"""
    def _generate(curr_row: int, cols: List[int], values: List[int]):
        for i in range(square.size):
            if i not in cols and square.get(curr_row, i) not in values:
                cols.append(i)
                values.append(square.get(curr_row, i))
                if curr_row == square.size-1:
                    yield (cols, values)
                else:
                    yield from _generate(curr_row+1, cols, values)
                cols.pop()
                values.pop()
    yield from _generate(0, [], [])


def generate_transversals(square: Square):
    """Generates all possible transversals for the given square"""
    for cols, _ in _generate_transversals(square):
        _square = Square(square.size)
        for i in range(square.size):
            _square.set(i, cols[i], 1)
        yield _square