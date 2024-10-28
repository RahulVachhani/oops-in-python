
# Bubble Sort

def bubble_sort(l1):

    for i in range(1,len(l1)):
        for j in range(len(l1)-i):
            if l1[j]> l1[j+1]:
                temp = l1[j]
                l1[j] = l1[j+1]
                l1[j+1] = temp
        print(l1)
    return l1

print(bubble_sort([10,30,60,22,20,40,33]))
