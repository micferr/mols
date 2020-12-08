from structures.square import Square


def generate_all_latin_squares_backtrack(square: Square, start_row: int, start_col: int, curr_row: int, curr_col: int):
    """Generates all latin squares through backtracking
    :param square: square instance, modified in place and passed through recursive calls
    :param start_row: first row to put elements in
    :param start_col: first column to put elements in
    :param curr_row: row of the element set in the current step
    :param curr_col: column of the element set in the current step
    """
    square_size = square.size

    for candidate in range(square_size):
        # Set current element to candidate
        square.set(curr_row, curr_col, candidate)

        # Check only current row and column for performance
        is_row_ok = len(set(square.data[curr_row][:curr_col + 1])) == curr_col + 1
        is_column_ok = len(set([square.data[row][curr_col] for row in range(curr_row + 1)])) == curr_row+1

        if is_row_ok and is_column_ok:
            # Square not yet filled, go on on filling elements
            if (curr_row, curr_col) != (square_size - 1, square_size - 1):
                next_row = curr_row if curr_col != square_size - 1 else curr_row + 1
                next_col = curr_col + 1 if curr_col != square_size - 1 else start_col

                yield from generate_all_latin_squares_backtrack(square, start_row, start_col, next_row, next_col)
            # Square is filled, yield it
            else:
                yield square


def generate_all_latin_squares(square_size: int, fixed_top=True, fixed_left=False):
    """Returns an iterator over all latin squares with given parameters
    :param square_size: size of the latin squares
    :param fixed_top: Whether to fix top row to 0,1,2,...,n-1
    :param fixed_left: Whether to fix leftmost column to 0,1,2,...,n-1 (applied only if fixed_top)
    """
    square = Square(square_size)

    start_row, start_col = 0, 0  # starting indexes for backtracking
    if fixed_top:
        square.data[0] = list(range(square_size))
        start_row = 1
        if fixed_left:
            for row in range(square_size):
                square.data[row][0] = row
            start_col = 1

    for s in generate_all_latin_squares_backtrack(square, start_row, start_col, start_row, start_col):
        yield s