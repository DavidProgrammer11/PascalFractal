from math import factorial


def binomial(n, k, mode=0):
    """
    Calculates each term of the binomial coefficient C(n, k).

    Args:
        n (int): Total number of elements.
        k (int): Number of chosen elements.
        mode (int): Output mode.
            0 -> returns the numeric value.
            1 -> returns Sierpiński display value (mod 5).

    Returns:
        int | str: The binomial coefficient or a display character.
    """
    result = (factorial(n) // (factorial(k) * (factorial(n - k))))
    if mode == 0:
        return result
    elif mode == 1:
        result = result % 5
        if result == 0:
            return " "
        else:
            return 1


def generate_diagonal(n, l):
    """
    Generates a diagonal of Pascal's triangle starting at row n.

    Args:
        n (int): Starting row index.
        l (int): Number of elements to generate.

    Returns:
        list: The diagonal values.
    """
    result_list = []
    if n >= 0 and l >= 0:
        for i in range(l):
            result_list.append(binomial(n + i, i, mode=0))
    return result_list

def create_triangle_row(x, mode=0):
    """
    Builds a single row of the triangle and appends it to the global list.

    Args:
        x (int): Row index.
        mode (int): Display mode (0 = Pascal, 1 = Sierpiński).
    """
    new_list = []
    for i in range(x + 1):
        new_list.append(binomial(x, i, mode))
    return new_list


def create(rows, mode=0):
    """
    Builds all rows of the triangle and returns them as a list.

    Args:
        rows (int): Number of rows to generate.
        mode (int): Display mode.
            0 -> Pascal's triangle.
            1 -> Sierpiński's triangle.

    Returns:
        list: A list of rows, each row being a list of values.
    """
    triangle = []
    for i in range(rows + 1):
        triangle.append(create_triangle_row(i, mode))
    return triangle

def draw_triangle(row_list):
    """
    Prints the triangle centered in the terminal.

    Args:
        row_list (list): List of rows to display.
    """
    global triangle
    max_width = len("   ".join(map(str, row_list[-1])))
    for i in range(len(row_list) - 1):
        row_str = "  ".join(map(str, row_list[i]))
        num_sep = (max_width - len(row_str)) // 2
        print(" " * num_sep + row_str)
    triangle = []


# Test
print(generate_diagonal(5, 7))
draw_triangle(create(20, 0))
draw_triangle(create(10, 1))
