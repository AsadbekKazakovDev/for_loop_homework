def main(A,B):
    """
    Return the numbers from A to B in the form of a list.
    Args:
        A: int
        B: int
    Returns:
        list: return  answer
    """
    ans=[]
    for i in range(A,B+1):
        ans.append(i)
    
    return ans
A,B = 2,7
print(main(A,B))