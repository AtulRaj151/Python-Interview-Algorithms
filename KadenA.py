def maxSubarraySum(A):
    max_current=max_global=A[0]
    for i in range(1,len(A)):

        print("max",max(A[i],max_current+A[i]))
        max_current=max(A[i],max_current+A[i])
        print("max current",max_current)
        if max_current>max_global:
            max_global=max_current
    return max_global
A=[-2,3,2,-1]
print(maxSubarraySum(A))

Outut:---------
    [3,2]
