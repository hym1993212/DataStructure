import sys

## a = sys.argv[1]
ops_rule = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2
}
##  input processing
def equation_input(raw_input):
    elem = []
    elem = raw_input.split()
    return elem

##  transition
def transition(elem):
    ##  stack to store operations
    stack = []
    ##  result to store the after sequence
    result = []
    for i in range(len(elem)):
        if elem[i] not in ["+","-","*","/","(",")"] and not elem[i].isdigit():
            return "Wrong input!"
        if elem[i] == "(":
            stack.append(elem[i])
        elif elem[i] == ")":
            while(len(stack) > 0):
                op = stack.pop()
                if op == "(":
                    break
                else:
                    result.append(op)

        ##  key part:
        ##  if the element is symbol
        elif elem[i] in ["+","-","*","/"]:
            while True:
                if stack == []:
                    stack.append(elem[i])
                    break
                op = stack.pop()
                ##  if the element has higher priority 
                if op == "(" or ops_rule[elem[i]] > ops_rule[op]:
                    stack.append(op)
                    stack.append(elem[i])
                    break
                else:
                    result.append(op)
                
        else:
            result.append(elem[i])

    while(len(stack) > 0):
        result.append(stack.pop())
        
    return result
            
            
            
def main():
    elem= []
    result = []
    raw_input = input("Please input:")
    elem = equation_input(raw_input)
    result = transition(elem)
    print(result)

if __name__ == "__main__":
    main()
