def main(A,B):
    """
    Return the sum of all integers from A to B.
    Args:
        A: int
        B: int
    Returns:
        int: return  answer
    """
    s=0
    for i in range(A,B):
        s+=i
    return s
A,B = 3,6
print(main(A,B))