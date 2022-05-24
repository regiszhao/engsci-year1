# # PROBLEM 1
# if __name__ == '__main__':
#     current_value = 0
#     print('Welcome to the calculator program.')
#     print('Current value:', current_value)


# PROBLEM 2-7
def display_current_value():
    print('Current value:', current_value)

def add(to_add):
    global current_value, prev_value
    prev_value = current_value
    current_value += to_add

def multiply(to_multiply):
    global current_value, prev_value
    prev_value = current_value
    current_value *= to_multiply

def divide(to_divide):
    global current_value, prev_value
    if to_divide != 0:
        prev_value = current_value
        current_value /= to_divide
    else:
        print('error division by zero')

def memory():
    global current_value, stored_value
    stored_value = current_value

def recall():
    print('Stored value:', stored_value)

def undo():
    global current_value, prev_value
    current_value, prev_value = prev_value, current_value


if __name__ == '__main__':

    current_value = 0
    stored_value = 'Error, no stored value.'
    prev_value = 'Error, no previous value.'
    display_current_value()





    

    # display_current_value()

    # add(10)
    # display_current_value()

    # multiply(2)
    # display_current_value()
    # memory()

    # divide(5)
    # display_current_value()

    # recall()

    # add(5)
    # display_current_value()

    # undo()
    # display_current_value()

    # multiply(4)
    # display_current_value()
    
    # undo()
    # undo()
    # display_current_value()


# PROBLEM 4
# Error occurs - the variable 'current_value' is not defined in the function 'add'

# PROBLEM 5
# Division by zero...?