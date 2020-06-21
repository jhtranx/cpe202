# Node list is
# None or
# Node(value, rest), where rest is the rest of the list
class Node:
    def __init__(self, value, rest):
        self.value = value
        self.rest = rest
    def __eq__(self, other):
        return ((type(other) == Node)
          and self.value == other.value
          and self.rest == other.rest
        )
    def __repr__(self):
        return ("Node({!r}, {!r})".format(self.value, self.rest))

# a StrList is one of
# - None, or
# - Node(string, StrList)

# StrList -> string
# Returns first (as determined by Python compare) string in StrList
# If StrList is empty (None), return None
# Must be implemented recursively
def first_string(strlist):
    if strlist is None:
        return None
    if strlist.rest == None:
        return strlist.value

    res = first_string(strlist.rest)
    if strlist.value < res:
        return strlist.value
    return res
    
# StrList -> (StrList, StrList, StrList)
# Returns a tuple with 3 new StrLists,
# the first one with strings from the input list that start with a vowel,
# the second with strings from the input list that start with a consonant,
# the third with strings that don't start with an alpha character
# Must be implemented recursively
def split_list(strlist):
    if strlist is None:
        return (None, None, None)
    res = split_list(strlist.rest)
    if strlist.value[0] in 'aeiouAEIOU':
        return (Node(strlist.value, res[0]), res[1], res[2])
    if strlist.value[0] in 'BbCcDdFfGgHhJjKkLlMmNnPpQqRrSsTtVvXxZzWwYy':
        return (res[0], Node(strlist.value, res[1]), res[2])
    if strlist.value[0] not in 'aeiouAEIOUBbCcDdFfGgHhJjKkLlMmNnPpQqRrSsTtVvXxZzWwYy':
        return (res[0], res[1], Node(strlist.value, res[2]))
