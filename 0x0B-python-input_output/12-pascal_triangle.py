#!/usr/bin/python3
"""
task 12
"""


def pascal_triangle(n):
    """
    Generates Piscal's triangle up to the specified level n
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]

        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])

        row.append(1)
        triangle.append(row)

    return triangle


if __name__ == "__main__":
    pass
