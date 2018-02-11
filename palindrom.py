
def palindrom(s):
    l = 0
    r = len(s)-1
    while l < r :
        if s[l] == s[r]:
            l += 1
            r -= 1
        else :
            rez = 'No'
            return rez
    rez = 'Yes'
    return rez

s= 'abyba'
print palindrom(s)

