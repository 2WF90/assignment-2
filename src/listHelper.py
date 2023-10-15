# strip removes all the zero elements at the end of the list 
# upto the first nonzero element.
#
# Args:
#   l: list of integers
# 
# Returns: stripped list of integers

def strip(l: list[int]) -> list[int]:
    # reverse iterate over l
    for i in range(len(l) - 1, -1, -1):
        if l[i] != 0:
            return l[:i + 1]
            
    return list()