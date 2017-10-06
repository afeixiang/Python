def cumsum(t):
    '''
    Calculate running total of integer list t

    t:integer list
    '''
    result = []
    i = 0
    for s in t:
        result.append(sum(t[:i+1]))
        i += 1
    print(result)

def middle(t):
    '''
    Return a list withour the first and the last items of t

    t:list
    '''
    print(t[1:len(t)-1])

def chop(t):
    ''''
    Modify list t remove the first and the last items

    t:list
    '''
    t.pop(0)
    t.pop(len(t)-1)

def is_sorted(t):
    ''''
    Modify list t remove the first and the last items

    t:list
    '''
    s = t[:]
    s.sort()
    return s == t

t = [1, 2, 3, 4]
e = [1, 2, 3, 4, 2]
f = ['a', 'c']
print(t)
print(is_sorted(t))
print(f)
print(is_sorted(f))
