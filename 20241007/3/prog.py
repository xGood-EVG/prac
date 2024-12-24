from math import * 
 
def Calc(s, t, u): 
    return lambda x: eval(u.replace('x', str(eval(s))).replace('y', str(eval(t)))) 
 
n = input() 
s, t, u = map(lambda x: x.strip().strip('"'), n.split(',')) 
x = eval(input()) 
calc_function = Calc(s, t, u) 
print(calc_function(x))