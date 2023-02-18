#raising exceptions

x = int(input('enter a number: '))
if x < 0:
    raise Exception('x should be positive')
else:
    print(x)
    
y =  8
assert (y>=0), 'x is not positive'


class Value_high(Exception):
    pass

class Value_small(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value
        
def test(x):
    if x > 100:
        raise Value_high('This value is too high')
    if x < 5:
        raise Value_small('This value is too small', x)

try:
    test(3)
except Value_high as e:
    print(e)
except Value_small as e:
    print(e.message, e.value)