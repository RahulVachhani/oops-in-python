
# Linear Search

def linear_search(l1, n):
    for i in range(len(l1)):
          if l1[i] == n:
               return i 
    return -1


a = [10,3,26,45,22,15,35]

pos = linear_search(a,45)

if pos != -1:
    print(f'The element is found at index : {pos}')
else:
    print('The element is not found')

