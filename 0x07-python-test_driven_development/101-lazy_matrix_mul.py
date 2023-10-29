#!/usr/bin/python3
"""
This module multiply 2 matrices using numpy module
"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """
    multiply 2 matrix that are given
    Args:
        m_a: input the first matrix
        m_b: input the second matrix
    Returns:
        return m_a * m_b
    """
    return numpy.matmul(m_a, m_b)

