#!/usr/bin/python3
"""Module Name: lazy_matrix_mul
This module does Matrix multiplication using NumPy.
"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """returns the result of Multiplying matrix 
    m_a and m_b using matmul.
    """
    return numpy.matmul(m_a, m_b)
