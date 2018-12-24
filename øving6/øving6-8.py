def count_coins(coins):
	total=0
	for element in coins:
		total+=element
	return total

mynter=[20,10,10,20,5,5,5,1,1]
print(count_coins(mynter))

#alternativ metode fra fasit:
def countCoins(coins):
	count = [0,0,0,0]   
	count[0] = coins.count(20)
	count[1] = coins.count(10)
	count[2] = coins.count(5)
	count[3] = coins.count(1)  
	return count
print(count_coins(mynter))


def num_coins(numbers):
	tjue=0
	ti=0
	fem=0
	en=0
	while numbers>=20:
		numbers-=20
		tjue+=1
	while numbers>=10:
		numbers-=10
		ti+=1
	while numbers>=5:
		numbers-=5
		fem+=1
	while numbers>=1:
		numbers-=1
		en+=1
	return [tjue,ti,fem,en]

print(num_coins(55))
print(num_coins(127))

def check_weight(numbers):
	vekt=0
	while numbers>=20:
		numbers-=20
		vekt+=9.9
	while numbers>=10:
		numbers-=10
		vekt+=6.8
	while numbers>=5:
		numbers-=5
		vekt+=7.85
	while numbers>=1:
		numbers-=1
		vekt+=4.35
	return round(vekt,4)

print(check_weight(67))
print(check_weight(125))
	