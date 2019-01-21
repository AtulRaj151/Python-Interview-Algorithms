class Solution:
    def spiralM(self,M):
        row_Begin=0
        row_End=len(M)-1
        col_Begin=0
        col_End=len(M[0])-1
        res=[]
        if len(M)==0:
            return res
        while(row_Begin<=row_End and col_Begin<=col_End):
            for i in range(col_Begin,col_End+1):
                res.append(M[row_Begin][i])
            row_Begin+=1
            for i in range(row_Begin,row_End+1):
                res.append(M[i][col_End])
            col_End-=1
            for i in range(col_End,col_Begin-1,-1):
                res.append(M[row_End][i])
            row_End-=1
            if col_Begin<=col_End:
                for i in range(row_End,row_Begin-1,-1):
                    res.append(M[i][col_Begin])
            col_Begin+=1
        return res
M=[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]
a=Solution()
print(a.spiralM(M))
output::[1,2,3,4,5,10,15,13,12,11,6,7,8,9]
