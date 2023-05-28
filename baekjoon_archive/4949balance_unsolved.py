'''
import re


def balanced_world(string):
    is_balanced = "yes"
    my_stack = []
    
    open_bracket = ['(', '[']
    close_bracket = [')', ']']
    
    braket_list = list(re.sub(r"[^\(\)\[\]]", '', string))
        
    for idx, bracket in enumerate(braket_list):
        if bracket in open_bracket:
            my_stack.append(bracket)
        elif bracket in close_bracket:
            index = close_bracket.index(bracket)
            
            if len(my_stack) > 0 and my_stack[-1] == open_bracket[index]:
                my_stack.pop()
            else:
                is_balanced = "no"
                break
    if len(my_stack) != 0:
        is_balanced = "no"
            
    return is_balanced
    
    
if __name__ == "__main__":
    while True:
        string = input()
        if string == ".":
            break
        print(balanced_world(string))
'''