"""Computation of weighted average of squares."""
from argparse import ArgumentParser

def average_of_squares(list_of_numbers, list_of_weights=None):
    """ Return the weighted average of a list of values.
    
    By default, all values are equally weighted, but this can be changed
    by the list_of_weights argument.
    
    Example:
    --------
    >>> average_of_squares([1, 2, 4])
    7.0
    >>> average_of_squares([2, 4], [1, 0.5])
    6.0
    >>> average_of_squares([1, 2, 4], [1, 0.5])
    Traceback (most recent call last):
    AssertionError: weights and numbers must have same length

    """
    if list_of_weights is not None:
        assert len(list_of_weights) == len(list_of_numbers), \
            "weights and numbers must have same length"
        effective_weights = list_of_weights
    else:
        effective_weights = [1.0] * len(list_of_numbers)
    squares = [
        weight * number * number / len(effective_weights)
        for number, weight
        in zip(list_of_numbers, effective_weights)
    ]
    return sum(squares)


def read_numbers_from_file(filename):
    """Read a list of numbers from a file."""
    with open(filename, 'r') as file:
        # Split the first line into numbers and convert them to floats
        numbers = file.readline().split()
    return [float(number) for number in numbers]


if __name__ == "__main__":
    parser = ArgumentParser(description="Compute the weighted average of squares of numbers from a file.")
    parser.add_argument(
        "file_numbers",
        metavar="FILE_NUMBERS",
        type=str,
        help="File containing a list of numbers (space-separated) to compute the weighted average of squares."
    )
    parser.add_argument(
        "--weights",
        metavar="FILE_WEIGHTS",
        type=str,
        help="Optional file containing a list of weights (space-separated)."
    )
    args = parser.parse_args()
    
    # Read numbers from file
    numbers = read_numbers_from_file(args.file_numbers)
    
    # Read weights from file if provided
    if args.weights:
        weights = read_numbers_from_file(args.weights)
    else:
        weights = None  # Default to equal weights

    result = average_of_squares(numbers, weights)
    
    print(result)
