#raising exceptions

x = int(input('enter a number: '))
if x < 0:
    raise Exception('x should be positive')
else:
    print(x)
    
y =  8
assert (y>=0), 'x is not positive'