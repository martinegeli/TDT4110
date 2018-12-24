
#Solve bubblesort without recursion
def bubble_sort(A):
    swap = True
    while swap:
        swap = False
        for i in range(1,len(A)):
            if A[i-1] > A[i]:
                temp = A[i]
                A[i] = A[i-1]
                A[i-1] = temp
                swap = True
    return A

liste = [9,1,34,7,2,3,45,6,78,56,36,65,33,21,23,34,45,6]
print(bubble_sort(liste))

#Solve bubblesort with recursion
def bubble_sort_rec(A):
    for i in range(1,len(A)):
        if A[i-1] > A[i]:
            temp = A[i]
            A[i] = A[i - 1]
            A[i - 1] = temp
            bubble_sort_rec(A)
    return A

list = [9,1,34,7,2,3,45,6,78,56,36,65,33,21,23,34,45,6,7,8]
print(bubble_sort_rec(list))


#Solve selection sort without recursion
def selection_sort(A):
    b = []
    for i in range(len(A)):
        b.insert(0,A.pop(A.index(max(A))))
    return b

lis = [9,1,34,7,2,3,45,6,78,56,36,65,33,21,23,34,45,6,7,8,19,24,3,28]
print(selection_sort(lis))

#Solve selection_sort with recursion
def selection_sort_rec(A, b = []):
    if len(A) < 1:
        return
    b.append(A.pop(A.index(max(A))))
    selection_sort_rec(A, b)
    return b[::-1]

l = [9,1,34,7,2,3,45,6,78,56,36,65,33,21,23,34,45,6]
print(selection_sort_rec(l))


j = 0
z = "Z"
for i in range(1,12):
    print((i-j)*z)
    if i > 5:
        j += 2