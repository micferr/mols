class Square:
    def __init__(self, size):
        """Inits a 0-filled square of given size.
        :param size: size of the square
        :returns: the newly created Square
        """
        self.data = []
        for i in range(size):
            self.data.append([0]*size)
        self.size = size

    def copy(self):
        """Returns a copy of this square
        :returns: a copy of this square
        """
        copy = Square(self.size)
        for i in range(self.size):
            for j in range(self.size):
                copy.set(i,j,self.get(i,j))
        return copy

    # Todo proper get/set
    def get(self, i: int, j: int) -> int:
        """Returns the element at position (i,j)"""
        return self.data[i][j]

    def set(self, i: int, j: int, val: int):
        """Sets the element at position (i,j)"""
        self.data[i][j] = val

    def get_row(self, row):
        return self.data[row]

    def get_column(self, column):
        return [self.data[row][column] for row in range(self.size)]

    def __str__(self):
        return "\n".join([",".join([str(element) for element in row]) for row in self.data])

    def is_latin(self, verbose:bool = False) -> bool:
        """Given a latin square, checks whether it is latin.
        The function returns True for latin squares with values in [0,n).
        :param verbose: if the square is not latin, whether to print the reason
        :returns: whether the square is latin
        """
        # Sanity check: all digits in [0,n)
        for row_index, row in enumerate(self.data):
            for col_index, elem in enumerate(row):
                if elem not in range(self.size):
                    if verbose:
                        print(f"Square element at position ({row_index},{col_index}) has value {elem}, "
                              f"square has size={self.size}.")
                    return False

        # Check rows
        for row_index, row in enumerate(self.data):
            num_distinct = len(set(row))
            if num_distinct != self.size:
                if verbose:
                    print(f"Row {row_index} has {num_distinct} distinct elements rather than {self.size}. "
                          f"Full row: {row}")
                return False

        # Check columns
        for col_index in range(self.size):
            column = [self.data[row][col_index] for row in range(self.size)]
            num_distinct = len(set(column))
            if num_distinct != self.size:
                if verbose:
                    print(f"Column {col_index} has {num_distinct} distinct elements rather than {self.size}. "
                          f"Full column: {column}")
                return False

        return True
