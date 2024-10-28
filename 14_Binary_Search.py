

# # Using Recursion

# def binary_search(l1, n, left, right):

#     if left > right:
#         return -1
    
#     mid = (left+right)//2
    
#     if l1[mid] == n:
#         return mid
#     elif l1[mid] < n:
#         left = mid + 1
#         return binary_search(l1,n,left, right)
#     else:
#         right = right - 1
#         return binary_search(l1, n, left, right)



# l1 = [10,20,30,40,50,60,70]
# print(binary_search(l1,20,0,len(l1)-1))



# Using loop

def binary_search(l1,n):

    left = 0
    right = len(l1)-1
    
    while left <= right:
        mid = (left + right)//2

        if l1[mid] == n:
            return mid
        elif l1[mid] < n:
            left = mid + 1
        else:
            right = mid -1
    return -1

l1 = [10,20,30,40,50,60,70]
print(binary_search(l1,60))
