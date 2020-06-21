from stack_array import Stack

# You do not need to change this class
class PostfixFormatException(Exception):
    pass

def postfix_eval(input_str):
    '''Evaluates a postfix expression
    
    Input argument:  a string containing a postfix expression where tokens 
    are space separated.  Tokens are either operators + - * / ** >> << or numbers.
    Returns the result of the expression evaluation. 
    Raises an PostfixFormatException if the input is not well-formed
    DO NOT USE PYTHON'S EVAL FUNCTION!!!'''
    stack = Stack(30)
    tokens = input_str.split()
    for item in tokens:
        if is_number(item):
            stack.push(eval_number(item))
        if is_operator(item):
            #pop two numbers from the stack
            try:
                number2 = stack.pop()
                number1 = stack.pop()
            except:
                raise PostfixFormatException("Insufficient operands")
            #evaluate based on operator
            if item == '+':
                returnItem = number1 + number2
                stack.push(returnItem)
            elif item == '-':
                returnItem = number1 - number2
                stack.push(returnItem)
            elif item == '*':
                returnItem = number1 * number2
                stack.push(returnItem)
            elif item == '/':
                #catches value error when dividing by zero
                if number2 == 0:
                    raise ValueError
                returnItem = number1 / number2
                stack.push(returnItem)
            elif item == '**':
                returnItem = number1 ** number2
                stack.push(returnItem)
            elif item == '>>':
                try:
                    returnItem = number1 >> number2
                    stack.push(returnItem)
                except:
                    raise PostfixFormatException("Illegal bit shift operand")
            elif item == '<<':
                try:
                    returnItem = number1 << number2
                    stack.push(returnItem)
                except:
                    raise PostfixFormatException("Illegal bit shift operand")
        if not (is_number(item) or is_operator(item)):
            raise PostfixFormatException("Invalid token")
    #returning final answer
    result = stack.pop()
    if not stack.is_empty():
        raise PostfixFormatException("Too many operands")
    else:
        return result

def is_number(s):
    '''Checks if item is a number
    Returns True if yes
    Returns False if no'''
    try:
        float(s)
        return True
    except ValueError:
        return False

def eval_number(s):
    '''Evaluates if number is either a float or int'''
    if "." in s:
        return float(s)
    return int(s)

def is_operator(s):
    '''Checks if item is an operator'''
    if s in "+ - * / ** >> <<":
        return True
    return False

def eval_precedence(s):
    '''Returns a number based on precedence of operator
    4 is highest, 1 is lowest'''
    if s == "<<":
        return 4
    if s == ">>":
        return 4
    if s == "**":
        return 3
    if s == "*":
        return 2
    if s == "/":
        return 2
    if s == "+":
        return 1
    if s == "-":
        return 1


def infix_to_postfix(input_str):
    '''Converts an infix expression to an equivalent postfix expression

    Input argument:  a string containing an infix expression where tokens are 
    space separated.  Tokens are either operators + - * / ** >> << parentheses ( ) or numbers
    Returns a String containing a postfix expression '''
    rpnList = []
    stack = Stack(30)
    tokens = input_str.split()

    for item in tokens:
        #when you encounter a number
        if is_number(item):
            rpnList.append(item)
        
        #when you encounter open paren
        elif item == '(':
            stack.push(item)
        #when you encounter closed paren
        elif item == ')':
            #pop stack until open paren and then
            while stack.peek() != '(':
                operator = stack.pop()
                rpnList.append(operator)
            if stack.peek() == '(':
                stack.pop()
            
        #when you encounter an operator and there nothing in the stack
        elif is_operator(item) and stack.is_empty():
            stack.push(item)
        
        #when you encounter an operator and theres only open paren in the stack
        elif (is_operator(item)) and (stack.peek() == "("):
            stack.push(item)

        #when you encounter an operator and there is another operator on top of stack
        elif is_operator(item) and is_operator(stack.peek()): 
            #while first operator is LEFT associative AND precedence is less than or equal to of second operator
            while (item != "**") and (not stack.is_empty()) and (stack.peek() != '(') and (eval_precedence(item) <= eval_precedence(stack.peek())):
                operator = stack.pop()
                rpnList.append(operator)
            #while first operator is RIGHT associative AND precedence is less than second operator
            while (item == "**") and (not stack.is_empty()) and (stack.peek() != '(') and (eval_precedence(item) < eval_precedence(stack.peek())):
                operator = stack.pop()
                rpnList.append(operator)
            stack.push(item)

    #popping the rest of the stack
    while not stack.is_empty():
        operator = stack.pop()
        rpnList.append(operator)
    
    #joining the list and making the return expression
    rpnExpression = " ".join(rpnList)
    return rpnExpression


def prefix_to_postfix(input_str):
    '''Converts a prefix expression to an equivalent postfix expression
    
    Input argument:  a string containing a prefix expression where tokens are 
    space separated.  Tokens are either operators + - * / ** >> << parentheses ( ) or numbers
    Returns a String containing a postfix expression(tokens are space separated)'''
    stack = Stack(30)
    reverse_tokens = input_str.split()
    #reverse tokens to go right to left
    reverse_tokens.reverse()

    for item in reverse_tokens:
        #when you encounter a number
        if is_number(item):
            stack.push(item)
        
        #when you encounter an operator
        elif is_operator(item):
            #pop two operands(numbers) from the stack
            op1 = stack.pop()
            op2 = stack.pop()

            #creating a new string with 2 operands from stack and 1 operator
            string = ' '.join([op1 ,op2 , item])
            stack.push(string)

    #returning final answer
    result = stack.pop()
    return result
