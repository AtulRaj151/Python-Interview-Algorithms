def findPivot(A,l,h):
    mid=int((l+h)/2)
    if A[mid]>A[mid+1]:
        return mid
    if A[mid]>A[l]:
        findPivot(A,mid+1,h)
    else:
        findPivot(A,l,mid-1)
    return -1

def BinarySearch(A,t,l,h):
    mid=int((l+h)/2)
    if A[mid]==t:
        return mid
    elif A[mid]>t:
        return BinarySearch(A,t,l,mid-1)
    else:
        return BinarySearch(A,t,mid+1,h)
A=[9,10,13,15,18,35,37,2,3,4,5,7,8]
piv=findPivot(A,0,12)
l=0
h=12
t=5

if A[piv]>t and A[l]>t:
    l=piv+1
elif A[piv]>t and A[l]<t:
    h=piv-1
print(A[BinarySearch(A,5,l,h)])
