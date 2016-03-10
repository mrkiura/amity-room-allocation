

def get_next(ls):
    '''
    Should return the next item on
    the list ls
    '''
    max = len(ls)
    cur = 0
    while min <= max:
        yield ls[cur]
        cur += 1
