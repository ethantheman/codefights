def firstDuplicate(a):
# this is a O(n) solution which uses O(1) memory to find the first duplicate number in an array for which the second occurrence has the minimal index.
# note that the array is expected to only contain numbers in the range from 1 to a.length 
    visited = set()
    for i in a:
        if i in visited:
            return i
        visited.add(i)
    return -1