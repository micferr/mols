from argparse import ArgumentParser
from pathlib import Path
import os

from helpers.latin import generate_all_latin_squares

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
