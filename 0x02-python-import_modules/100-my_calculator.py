#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    from calculator_1 import add, sub, mul, div

    argv_len = len(sys.argv) - 1
    if not argv_len == 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>", end='\n')
        exit(1)
    argv_elem = sys.argv[1:]
    operators = "+-/*"
    operator = argv_elem[1]
    if operator not in operators:
        print("Unknown operator. Available operators: +, -, * and /", end='\n')
        exit(1)
    a = int(argv_elem[0])
    b = int(argv_elem[2])
    ops = [add, sub, mul, div]
    ch = 0
    if operator == '+':
        ch = 0
    if operator == '-':
        ch = 1
    if operator == '*':
        ch = 2
    if operator == '/':
        ch = 3
    f_str = "{0:d} {1} {2:d} = {3:d}".format(a, operator, b, ops[ch](a, b))
    print(f_str, end='\n')
