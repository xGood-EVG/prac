from math import * 
 
def Calc(s, t, u): 
    return lambda x: eval(u.replace('x', str(eval(s))).replace('y', str(eval(t)))) 
 
n = input() 
s, t, u = map(lambda x: x.strip().strip('"'), n.split(',')) 
<<<<<<< HEAD
x = eval(input()) 
=======
x = float(input()) 
>>>>>>> f7e4e7c4a572a19379eb7d9366907d89bccf405a
calc_function = Calc(s, t, u) 
print(calc_function(x))