def main(n):
    """
    Return numbers from zero to n in a string view.
    Args:
        n: int
    Returns:
        string: return  answer
    """
    s=""
    for i in range(n+1):
        s+=str(i)
    a = list(s)
    return ",".join(a)
n = 5
print(main(n))