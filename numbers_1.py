#Using python as a calculator

'''

We can use the interpreter to take an input and return an output!

Arithmetic Operators:
We have a whole bunch of operators at our disposal
+ Addition
- Subtraction
* Multiplication
/ Division
// Floor division
% Modulus (remainder of x/y) | use divmod(x,y)
** Exponentiation (power of) | can also use pow(x,y) instead of x**y

Assignment Operators:
= Equals

Number Types:
int (2, 4, 8)
float (2.1, 4.5, 8.05)

Build in Function:
round() Rounds a number with the specified number of decimals i.e. round(num, decimals)

40000000 = 40_000_000
'''

addition = 2 + 2
print(addition)
sub = 45 - 16
print (sub)
mul = 4 * 8
div = 10/4
floors = 10//4
mod = 10%6
divm = divmod(10,6)
po = 5 ** 7
po_1 = pow(2,7)
print(mul, po, po_1, floors, divm,mod)
#the last printed expression is assigned to the variable _
tax = 12.5/100
price = 100.50
price * tax # this is assigned to a variable _
price + _
round(_,2)