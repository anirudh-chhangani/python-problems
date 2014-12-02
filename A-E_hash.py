__author__ = 'dell'


def hash(S):
    result = number of characters 'A' in S
    if |S| > 1:
        (S1, S2) = split(S)
        result = result + max(hash(S1), hash(S2))
        return result

def split(S):
