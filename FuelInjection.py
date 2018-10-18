def helper(n,diction):
    if(n in diction):
        return diction[n]
    if(n%2 != 0):
        diction[n] = min(helper(((n+1)/2),diction) +2,helper(((n-1)/2),diction)+2)
    else:
        diction[n] = helper((n / 2),diction) + 1
    return diction[n]
def answer(n):
    # your code here
    num = int(n)
    
    diction = {}
    diction[1] = 0
    diction[2] = 1
    return helper(num,diction)
    