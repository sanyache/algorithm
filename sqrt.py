
def sqrt(n):
    n = float(n)
    right = n
    left = float(0)
    middle = float((right+left)/2)
    while (right-left) > 0.0001 :
        if (middle**2) >= n :
            right = middle
        else:
            left = middle
        middle = (right+left)/2
    if(n-right**2)< (n-left**2):
        rez = right
    else:
        rez = left
    return  rez

n = 25
print (sqrt(n))