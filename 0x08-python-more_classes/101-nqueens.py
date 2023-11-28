#!/usr/bin/python3
"""
Module Name: 101-nqueens
This module resolves the N-Queen puzzle
using backtracking
"""


def canKill(queen_locs_arr, nqueen):
    """ Method determines that queens can or can't kill each other

    Args:
        queen_locs_arr: array that has the queens positions
        nqueen: queen number

    Returns: Either true or false depending.
    """

    for idx in range(nqueen):
        if queen_locs_arr[idx] == queen_locs_arr[nqueen]:
            return False
        if abs(queen_locs_arr[idx] - queen_locs_arr[nqueen]) == abs(idx - nqueen):
            return False
    return True


def disp_result(queen_locs_arr, nqueen):
    """ Method that prints the list with the Queens positions

    Args:
        queen_locs_arr: array that has the queens positions
        nqueen: queen number
    """
    queen_locs = []
    for idx in range(nqueen):
        queen_locs.append([idx, queen_locs_arr[idx]])
    print(queen_locs)

def Queen(queen_locs_arr, nqueen):
    """ Recursive function that executes the Backtracking algorithm

    Args:
        queen_locs_arr: array that has the queens positions
        nqueen: queen number
    """

    if nqueen is len(queen_locs_arr):
        disp_result(queen_locs_arr, nqueen)
        return

    queen_locs_arr[nqueen] = -1
    while((queen_locs_arr[nqueen] < len(queen_locs_arr) - 1)):
        queen_locs_arr[nqueen] += 1
        if canKill(queen_locs_arr, nqueen) is True:
            if nqueen is not len(queen_locs_arr):
                Queen(queen_locs_arr, nqueen + 1)


def resolveQueen(size):
    """ Function that invokes the Backtracking algorithm

    Args:
        size: size of the chessboard
    """
    queen_locs_arr = [-1 for idx in range(size)]
    Queen(queen_locs_arr, 0)


if __name__ == '__main__':

    import sys

    if len(sys.argv) == 1 or len(sys.argv) > 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        size = int(sys.argv[1])
    except:
        print("N must be a number")
        sys.exit(1)

    if size < 4:
        print("N must be at least 4")
        sys.exit(1)
    resolveQueen(size)
