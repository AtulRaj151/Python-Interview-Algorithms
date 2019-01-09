#Given a set of candidates numbers (C) (without duplicates) and target numbers
# (T),find all the unique combination in C where the candidates number sums to T
#the sane reoeated number may be chosen from C unlimited number of times
#Note::::
# All Number(including target will be positive integer and the solution set must
#not contain duplicates combination
#for example given candidates__ set [2,3,6,7] and target 7
#solution set is  [
#                  [7]
#                  [2,2,7]
#                 ]
#author:Atul Raj
class Combination:
    def combinationSum(self,candidate,target):
        candidate.sort()
        res=[]
        self.DFS(candidate,target,0,res,[])
        return res
    def DFS(self,candidate,target,start,res,intermediate):
        if target==0:
            res.append(intermediate)
            return
        for i in range(start,len(candidate)):
            if target<candidate[i]:
                return
            self.DFS(candidate,target-candidate[i],i,res,intermediate+[candidate[i]])
ob=Combination()

print(ob.combinationSum([2,3,2,1,6,7],6))
