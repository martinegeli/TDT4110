number_list = [i for i in range(1,101)]

summer = []
for i in number_list:
	if i%3==0 or i%10==0:
		summer.append(i)
print(sum(summer))

#One-line sum
result = sum([x for x in range(1,101) if x % 3 == 0 or x % 10 == 0])
print(result)

number_list[::2], number_list[1::2] = number_list[1::2], number_list[::2]
print(number_list)

reversed_list = number_list[::-1]
