from random import *
from collections import Counter

random = []
for i in range(100):
	random.append(randrange(1,11))

print('Antall av tall 2: ', random.count(2))

print('Summen av tallene er ', sum(random))

random.sort()
print('Listen sortert: ', random)

b=Counter(random)
c=b.most_common(1)
print(c)
print(b)

random.reverse()
print('Listen reversert: ', random)
