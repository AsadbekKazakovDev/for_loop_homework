def main(A,B):
    """
    Return the numbers from B to A in the form of a list.
    Args:
        A: int
        B: int
    Returns:
        list: return  answer
    """
    if A<B:
        ans=[]
        for i in range(B,A-1,-1):
            ans.append(i)
        return ans
A,B = 5,9
print(main(A,B))