from argparse import ArgumentParser
from pathlib import Path
import os

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
    """ Returns an iterator over all latin squares with given parameters
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



if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--size", type=int, default=4, help="Size of the latin squares")
    parser.add_argument("--onefile", action='store_true', help="Store all squares in one file, separated by an empty line")
    parser.add_argument("--fixed-top", action='store_true', help="Fix top row to 0,1,2,...,n-1")
    parser.add_argument("--fixed-left", action='store_true', help="Fix leftmost column to 0,1,2,...,n-1 (only if also fixed top)")
    parser.add_argument("--silent", action="store_true", help="Avoid also printing all squares to stdout")
    parser.add_argument("--out", type=str, default='./out')

    args = parser.parse_args()
    square_size = args.size
    fixed_top, fixed_left = args.fixed_top, args.fixed_left

    # Create output folder
    Path(args.out).mkdir(parents=True, exist_ok=True)

    square_generator = enumerate(generate_all_latin_squares(square_size, fixed_top, fixed_left))

    if not args.onefile:
        for i, square in square_generator:
            if not args.silent:
                print(f"{square}\n")
            with open(os.path.join(args.out, f"{i}.csv"), "w") as fout:
                fout.write(f"{str(square)}\n\n")
    else:
        with open(os.path.join(args.out, "out.csv"), "w") as fout:
            for i, square in square_generator:
                if not args.silent:
                    print(f"{square}\n")
                fout.write(f"{str(square)}\n\n")
