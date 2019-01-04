def binS(A,target):
    low=0
    high=len(A)-1
    while low<=high:
        mid=(high+low)//2
        if A[mid]==target:
            return mid
        elif A[mid]>target:
            high=mid-1
        else:
            low=mid+1
    return low
A=[1,2,4,5,6]
print(binS(A,6))
