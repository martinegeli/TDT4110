import random

def numbersfunc():
    return [i for i in range(1,35)]

numbers = numbersfunc()

def myGuess():
    result = []
    i = 0
    while i < 7:
        r = random.randint(1,34)
        if r not in result:
            result.append(r)
            i += 1
    return result

#print(myGuess())

def drawNumbers(numbers, n):
    result = []
    i = 0
    while i < n:
        r = random.randint(0,len(numbers)-1)
        if r not in result:
            result.append(numbers[r])
            i += 1
    return result

draw = drawNumbers(numbers, 7)
#print(draw)

def compList(draw, myGuess):
    like_lotto = 0
    like_tillegg = 0
    tall_lotto = draw[0:7]
    tall_tillegg = draw[7:10]
    for item in myGuess:
        if item in tall_lotto:
            like_lotto += 1
        elif item in tall_tillegg:
            like_tillegg += 1
    return like_lotto, like_tillegg

def winnings(like_lotto, like_tillegg):
    dict = {(7,0) : 2749455,
			(6,1):102110,
			(6,0):3385,
			(5,2):95,
			(5,1):95,
			(5,0):95,
			(4,3):45,
			(4,2):45,
			(4,1):45,
		}
    l = (like_lotto, like_tillegg)
    if l in dict:
        print((like_lotto, like_tillegg), dict.get(l))
        return dict.get(l) - 5
    return -5


def main():
    numbers = numbersfunc()
    my_guess = myGuess()
    print(my_guess)

    total = 0
    for i in range(1000000):
        draw = drawNumbers(numbers, 10)
        like_lotto, like_tillegg = compList(draw, my_guess)
        total += winnings(like_lotto, like_tillegg)
    print(total)

#main()
