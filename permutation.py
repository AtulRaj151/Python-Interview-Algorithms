def swap(l,x,y):
    l[x],l[y]=l[y],l[x]
def perm(l,i):
    l2=dict()
    if i == len(l):
        print(l)

    else:
        for j in range(i,len(l)):
            swap(l,i,j)
            perm(l,i+1)
            swap(l,i,j)
l=['ab','ab','cd']
print(perm(l,0))
