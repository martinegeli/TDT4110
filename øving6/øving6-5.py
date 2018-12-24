number_list=[0+i for i in range(100)]
print(number_list)

summer=[]
for i in number_list:
	if i%3==0 or i%10==0:
		summer.append(i)
print(sum(summer))
	
number_list[::2], number_list[1::2]= number_list[1::2], number_list[::2]
print(number_list)

reversed_list=number_list[::-1]
print(reversed_list)