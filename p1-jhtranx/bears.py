# int -> booelan
# Given integer n, returns True or False based on reachabilty of goal
"""A True return value means that it is possible to win
the bear game by starting with n bears. A False return value means
that it is not possible to win the bear game by starting with n
bears.""" 

def bears(n):
    # base cases
    if n == 42:
        return True
    if n < 42:
        return False
    
    # steps
    if ((n % 2) == 0) and bears(n / 2): #checks if bears are divisible by 2
        return True
    if ((n % 5) == 0) and bears(n - 42): #checks if bears are divisible by 5
        return True
    if ((n % 3) == 0) or ((n % 4) == 0): #checks if bears are divisible by 3 or 4
        multiple = (n % 10)*(int(n / 10) % 10) 
        if multiple != 0: #stops infinite loop of 0
            if bears(n - multiple):
                return True
        return False #if the multiple of the two is 0, it is False
    return False

print(bears(430))