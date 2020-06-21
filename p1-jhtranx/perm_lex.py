# string -> List of strings
# Returns list of permutations for input string
# e.g. 'ab' -> ['ab', 'ba']; 'a' -> ['a']; '' -> []
def perm_gen_lex(str_in):
    # if str_in == []:
    #     return []

    # base cases
    if len(str_in) == 0:
        return []
    if len(str_in) == 1:
        return [str_in[0]]

    result_str = []

    # making simpler string
    for char in str_in:
        simple_str = ''
        for x in str_in:
            if x != char:
                simple_str = simple_str + x
        
        # recursive step
        remainder = perm_gen_lex(simple_str)
        for val in remainder:
            result_str.append(char + val)

    return result_str