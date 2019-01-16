class Solution:
    def jump(self,A):
        jump=0
        ladder=A[0]
        stair=A[0]
        for level in range(len(A)):
            if level==len(A)-1:
                return jump
            if(level+A[level]>=ladder):
                ladder=level+A[level]
            stair -=1
            if stair==0:
                jump +=1
                stair=A[level]-level
        return jump
A=[1,3,5,8,9,2,6,7,6,8,9]
b=Solution()
print(b.jump(A))
