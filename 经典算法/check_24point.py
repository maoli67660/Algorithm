"""
only works on integer
e.g. [1,3,4,6]	-- > (6/(1-(3/4)))=24 doesn't work because float numbers
"""

def reduce(ls):
    reduced_lists = []
    for i in range(len(ls)-1):
        reduced_lists.append(ls[:i] + [ls[i]+ls[i+1]] + ls[i+2:])
        reduced_lists.append(ls[:i] + [ls[i]-ls[i+1]] + ls[i+2:])
        reduced_lists.append(ls[:i] + [ls[i]*ls[i+1]] + ls[i+2:])
        if ls[i+1] != 0:
            reduced_lists.append(ls[:i] + [ls[i]/ls[i+1]] + ls[i+2:])
    return reduced_lists

def is_24_set(check_list):
    last_level_lists = [check_list]
    lists = []

    while len(last_level_lists[0]) >1:
        for ls in last_level_lists:
            lists.extend(reduce(ls))
        last_level_lists = lists
        lists = []   
    result_set = set()
    for item in last_level_lists:
        result_set.add(item[0])
    return 24 in result_set

if __name__ == '__main__':
    assert is_24_set([2,4,6,12])
    assert is_24_set([12,4,6,2])
    assert is_24_set([12,4,6,3])
    assert not is_24_set([1,1,1,3])
    
