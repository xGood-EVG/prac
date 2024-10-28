from math import *

functions = {}
line_count = 0
function_count = 0

while line := input():
    line_count += 1
    if line.startswith(":"):
        name, *args, formula = line[1:].split()
        functions[name] = (args, formula)
        function_count += 1
    elif line.startswith("quit "):
        print(eval(line[5:].format(function_count + 1, line_count)))
        break
    else:
        name = line.split()[0]
        args, formula = functions[name]
        if len(args) == 1:
            arg_values = line.split(" ", 1)
            locals()[args[0]] = eval(arg_values[1])
        else:
            arg_values = line.split()[1:]
            for i in range(len(args)):
                locals()[args[i]] = eval(arg_values[i])
        
        print(eval(formula, {}, locals()))
