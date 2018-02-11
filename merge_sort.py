
def create_arrey(len=10, max=50):
    from random import randint
    return  [randint(0,max) for _ in range(len)]

def merge(a,b):
    c = []
    i,j = 0,0
    while i<len(a) and j<len(b):
        if a[i]<b[j]:
            c.append(a[i])
            i+=1
        else:
            c.append(b[j])
            j+=1
    if i == len(a) :
        c.extend(b[j:])
    else:
        c.extend(a[i:])
    return c
def merge_sort(a):
    if len(a) <= 1:
        return(a)
    left,right = merge_sort(a[:len(a)/2]),merge_sort(a[len(a)/2:])
    return merge(left,right)
a = create_arrey()
print a
print merge_sort(a)


