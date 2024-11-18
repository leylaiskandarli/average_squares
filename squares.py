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
        effective_weights = [1] * len(list_of_numbers)
    squares = [
        weight * number * number
        for number, weight
        in zip(list_of_numbers, effective_weights)
    ]
    return sum(squares)


def convert_numbers(list_of_strings):
    """Convert a list of strings into numbers, ignoring whitespace.
    
    Example:
    --------
    >>> convert_numbers(["4", " 8 ", "15 16", " 23    42 "])
    [4, 8, 15, 16]

    """
    all_numbers = []
    for s in list_of_strings:
        # Take each string in the list, split it into substrings separated by
        # whitespace, and collect them into a single list...
        all_numbers.extend([token.strip() for token in s.split()])
    # ...then convert each substring into a number
    return [float(number_string) for number_string in all_numbers]

# Work here 
if __name__ == "__main__":
    parser = ArgumentParser(description="Calculate the weighted average of squares of a function")

    # Positional argument for numbers
    parser.add_argument(
        "numbers",
        metavar="N",
        type=float,
        nargs="+",
        help="A sequence of numbers for which to calculate the weighted average of squares."
    )
    
    # Optional argument for weights
    parser.add_argument(
        "--weights",
        metavar="W",
        type=float,
        nargs="+",
        help="A sequence of weights corresponding to the numbers. Must be the same length as the numbers."
    )
    
    args = parser.parse_args()

    # Read numbers and weights from command-line arguments
    numbers = args.numbers
    weights = args.weights

    # Check if weights were provided, else default to equal weights
    if weights is None:
        weights = [1] * len(numbers)
    elif len(weights) != len(numbers):
        raise ValueError("The number of weights must match the number of numbers.")

    #numbers_strings = ["1","2","4"]
    #weight_strings = ["1","1","1"]        
    
    #numbers = convert_numbers(numbers_strings)
    #weights = convert_numbers(weight_strings)
    
    result = average_of_squares(numbers, weights)
    
    print(result)