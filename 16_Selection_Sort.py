
# Selection Sort 

def selection_sort(l1):

    for i in range(len(l1)-1):
        
        min = i
        for j in range(i+1,len(l1)):
            if l1[j] < l1[min]:
                min = j
        if min != i:
            temp = l1[i]
            l1[i] = l1[min]
            l1[min] = temp
        print(l1)

    return l1 

print(selection_sort([10,222,20,34,2]))
