# collections: Counter, namedtuple, orderedDict, defaultDict, deque

from collections import Counter as c

a = "aaaaaabbbbccc"
my_counter = c(a)
print(my_counter)
print(my_counter.items())
print(my_counter.keys())
print(my_counter.values())
print(my_counter.most_common(1))
print(list(my_counter.elements()))

from collections import namedtuple as n

point =  n('Point', 'x,y')
pt = point(1, -4)
print(pt.x, pt.y)


from collections import OrderedDict as od
order = od()
order['a'] = 1
order['b'] = 2
order['c'] = 3
order['e'] = 5
order['d'] = 4
print(order)

from collections import defaultdict as d
din = d(int)
din['a'] = 1
din['b'] = 2
print(din['c'] ) # will return d default value of the tyupe specified (0 for int)


from collections import deque

deq = deque()

deq.append(1)
deq.append(2)

deq.appendleft(3)
print(deq)

deq.popleft()
print(deq)