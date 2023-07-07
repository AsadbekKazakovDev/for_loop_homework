def main(k,n):
    """
    Repeat the number k n times and return to the list view.
    Args:
        k: int
        n: int
    Returns:
        list: return  answer
    """
    ans=[]
    for i in range(1):
        ans.append(k)
    return ans*n
k,n = 5,3
print(main(k,n))