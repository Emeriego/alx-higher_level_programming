#!/usr/bin/python3

def magic_calculation(a, b):
    outcome = 0
    for item in range(1, 3):
        try:
            if item > a:
                raise Exception('Too far')
            else:
                outcome += a ** b / item
        except Exception:
            outcome = b + a
            break
    
    return outcome
