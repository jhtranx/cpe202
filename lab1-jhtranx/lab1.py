# CPE 202 Lab 1

# Maybe_List is either
# Python List
# or
# None

# Maybe_integer is either
# integer
# or
# None

# Maybe_List -> Maybe_integer
def max_list_iter(int_list):
   """finds the max of a list of numbers and returns the value (not the index)
   If int_list is empty, returns None. If list is None, raises ValueError"""
   if int_list == []:
      return None
   if int_list == None:
      raise ValueError
   max = int_list[0]
   for val in int_list:
      if val > max:
         max = val
   return max


# Maybe_List -> Maybe_List
def reverse_list(int_list):
   """reverses a list of numbers and returns the reversed list
   If list is None, raises ValueError"""
   if int_list == None:
      raise ValueError
   result = []
   for val in int_list:
      result.insert(0,val)
   return result


# Maybe_List -> None
def reverse_list_mutate(int_list):
   """reverses a list of numbers, modifying the input list, returns None
   If list is None, raises ValueError"""
   if int_list == []:
      return None
   if int_list == None:
      raise ValueError
   for i in range(len(int_list)):
      val = int_list[i]
      del int_list[i]
      int_list.insert(0,val)
   return int_list

# Maybe_List -> Maybe_List
def reverse_rec(int_list):   # must use recursion
   """recursively reverses a list of numbers and returns the reversed list
   May NOT mutate the original list. If list is None, raises ValueError"""
   if int_list == None:
      raise ValueError
   new_list = int_list
   if len(new_list) == 0:
      return []
   return [new_list[-1]] + reverse_rec(new_list[:-1])

