def edit_distance(s1, s2):
    '''(str, str) -> int
    function returns the min num of character changes needed to turn s1 into s2
    '''
    # if s1 is an empty str
    if s1 == '':
        distance = len(s2)
    # if s2 is an empty str
    if s2 == '':
        distance = len(s1)
    # if s1 and s1 are both single char strs
    elif (len(s1) == 1) and (len(s2) == 1):
        if s1 == s2:
            distance = 0
        else:
            distance = 1
    else:
        # check the first chars from both strings
        # and recurse on the rest of the string
        distance = (edit_distance(s1[:1], s2[:1])) + (
                      edit_distance(s1[1:], s2[1:]))
    return distance


def subsequence(s1, s2):
    '''(str, str) -> bool
    function that checks if s1 is a subsequence of s2
    '''
    # if s1 is the same as s2
    if s1 == s2:
        result = True
    # if s1 is empty
    elif s1 == '':
        result = True
    # if s2 is empty
    elif s2 == '':
        result = False
    # if the first char of s1 and s2 are the same
    # check the rest of the strings
    elif s1[0] == s2[0]:
        result = subsequence(s1[1:], s2[1:])
    # if the first char of s1 and s2 are different
    # check str 1 against the rest of str 2
    elif s1[0] != s2[0]:
        result = subsequence(s1, s2[1:])
    return result


def perms(s):
    '''(str) -> set of str
    function returns a list of all possible permutations using the characters
    in s
    '''
    # base case if length of str is less than or equal to 1
    # the permutation of the str is itself
    if len(s) <= 1:
        result = {s}
    else:
        # get all permutations of length N-1
        char = s[0]
        temp = perms(s[1:]) # returns a set of all permutation of s[1:]
        result = set()
        for perm in temp:
            for i in range(len(perm)+1):
                result.add(perm[i:] + char + perm[:i])
    return result
