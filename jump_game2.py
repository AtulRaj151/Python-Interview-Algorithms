 #In this concept we have used the concept of stair and ladder,we choose the maximum ladder and traverse the ladder hence we decrement the
 #stair ie.[3 2 1 1 4] in this we can jump the in 2 step in the last index example [3,1]
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
