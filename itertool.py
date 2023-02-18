#This is a collection of tools for handling iterators
#itertools: product, permutations, combinations, accumulate, groupby, and infinite iterators

from itertools import product
a = [1,2]
b = [3,4]
prod = product(a,b)
prod_rep = product(a,b, repeat=2)
print(list(prod))
print(list(prod_rep))

from itertools import permutations
a = [1,2,3]
perm = permutations(a)
print(list(perm))
permi = permutations(a, 2)
print(list(permi))

from itertools import combinations, combinations_with_replacement as cwr
a = [1,2,3,4]
comb = combinations(a, 2)
print(list(comb))
combine = cwr(a,2)
print(list(combine))

from itertools import accumulate
import operator
a = [1,2,3]
acc = accumulate(a)
print(a)
print(list(acc))
bas =  accumulate(a, func=operator.mul)
print(list(bas))
acd = accumulate(a, func=max)
print(list(acd))

from itertools import groupby
a = [1,2,3,4]

def smaller_than_3(x):
    return x < 3

group_obj = groupby(a, key=smaller_than_3)
for key, value in group_obj:
    print(key, list(value))

persons = [{'name': 'Tim', 'age': 25},
           {'name': 'Kim', 'age': 30},
           {'name': 'Tom', 'age': 22}, 
           {'name': 'Lisa', 'age': 20}]

groupp =  groupby(persons, key=lambda x: x['name'])
for key, value in groupp:
    print(key, list(value))
    
    
from itertools import count, cycle, repeat

for i in count(10):
    # start counting from 10
    print(i)
    if i == 20:
        break
    
a = [1,2,3,4,5,6]
for i in cycle(a):
    print(i)
    if i == 6:
        break
      
for i in repeat(6, 4):
    print(i)