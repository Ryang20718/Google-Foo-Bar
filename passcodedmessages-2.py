import copy
def recurse(arr,total):
    if(len(arr) == 0):
        if((total %3 == 0)):
            return total 
        else:
            return 0
    sean = []
    if(total %3 == 0):
        sean.append(total)
    for i in range(len(arr)):
        mod = copy.copy(arr)
        temp = total*10 + arr[i]
        del mod[i] 
        sean.append(recurse(mod,temp))
    return max(sean)
        
def answer(l):
    # your code here
    res = 0
    l.sort()
    if(len(l)==0):
        return 0
    if(len(l)==1):
        return l[0]
    return recurse(l,0)
    
    