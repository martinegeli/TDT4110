
def recursive_sum(n):
    if n == 1:
        return 1
    return n + recursive_sum(n-1)

#print(recursive_sum(5))

def fakultet(n):
    if n == 1:
        return 1
    return n * fakultet(n-1)

#print(fakultet(5))

def find_smallest_element(numbers, mini = float('inf')):
     if numbers[0] < mini:
        mini = numbers[0]
     if len(numbers) == 1:
        return mini
     print(mini)
     return find_smallest_element(numbers[1::], mini)


def find_smallest(numbers):
    if len(numbers) == 1:
        return numbers[0]
    smallest = numbers[0]
    find_small = find_smallest(numbers[::1])
    if find_small < smallest:
        find_small = smallest
    return find_small

liste = [10,7,5,11,13,4,7]
print(find_smallest_element(liste))
print(find_smallest(liste))

def binary_search(numbers, element, j, n):
    if element not in numbers:
        return (-float('inf'))
    mid = (j+n)//2
    if numbers[mid] == element:
        return mid
    elif numbers[mid] > element:
        return binary_search(numbers, element, j, mid)
    else:
        return binary_search(numbers, element, mid, n)

list = [1,2,3,4,5,8,19,21,23,25,26,29,41,47,56,93,2,20]
#print(binary_search(list, 56, 0, len(list)))

