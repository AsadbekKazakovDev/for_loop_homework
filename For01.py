import py_compile


def main(n):
    """
    Return numbers from zero to n in a list view.
    Args:
        n: int
    Returns:
        list: return  answer
    """
    ans =[]
    for i in range(n):
        ans.append(i)
    return ans
n = 5
print(main(n))