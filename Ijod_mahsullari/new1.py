# Binar qidirish
# def binar_search(list, item):
#     low = 0
#     high = len(list)-1
    
#     while low <= high:
#         mid = int((low + high)/2)
#         guess = list[mid]
#         if guess == item:
#             return mid
#         if guess > item:
#             high = mid - 1
#         else:
#             low = mid + 1
#     return None

# my_list = [1, 5, 7, 9, 12, 18]
# print(binar_search(my_list, 18))


# def moveZeroes(nums):
#     j = 0
#     list1 = []
#     for i in nums:
#         if i == 0:
#           j += 1
#         else:
#             list1.append(i)
#     for i in range(j):
#         list1.append(0)
#     return list1
# list2 = [0, 1, 0, 3, 12]
# print(moveZeroes(list2))            
        

# def ad(a, sum_value):
#     if len(a) == 1:
#         if a[0] == sum_value:
#             return []
#     else:
#         for i in range(len(a)):
#             for j in range(i + 1, len(a)):
#                 if a[i] + a[j] == sum_value:
#                     if a[i] < a[j]:
#                         return [a[i], a[j]]
#                     else:
#                         return [a[j], a[i]]
#     return []

# a = [1,15]
# sum_value = 16
# print(ad(a, sum_value))


# def isValidSubsequence(array, sequence):
#     a = 0
#     for i in array:
#         if a < len(sequence) and i == sequence[a]:
#             a+=1
#     return a == len(sequence)
        
# isValidSubsequence(array = [5, 1, 22, 25, 6, -1, 8, 10], sequence = [5, 2, 25])
        
# lambda
# def rotate(nums: list, k: int):
#     for i in range(k):
#         for j in nums:
#             if j == nums[-1]:
#                 nums.remove(j)
#                 nums.insert(0, j)
#     return nums
# print(rotate(nums=[1,2,3,4,5,6,7], k=4))

# def sortedSquaredArray(a):
#   a=list(map(lambda x:x**2,a) )
#   for i in range(len(a)):
#     for j in range(i,len(a)):
#       if a[i]>a[j]:
#         a[i],a[j]=a[j],a[i]
#   return   a   

# a=[-10, 1,5,3,2]
# print(sortedSquaredArray(a))


def tournamentWinner(competitions, results):
  a=[]
  for i in range(len(results)):
    if results[i]==0:
      a.append(competitions[i][1])
    else:
      a.append(competitions[i][0])
  b={}
  for i in a:
    if b.get(i) ==None:
      b.update({i:1})
    else:
      b[i] = b.get(i) + 1
  q=0
  p=''   
  for key, value in b.items():
    if q<value:
      p=key
      q=value

  return p
  # print(key)
  # print(value)
        


competitions = [
  ["HTML", "C#"],
  ["C#", "Python"],
  ["Python", "HTML"],
]
results = [0, 0, 1]       
print(tournamentWinner(competitions,results))
# scores = {"Alice": 90, "Bob": 85, "Charlie": 92}

# # Accessing an existing key
# print(f"Alice's score: {scores.get('Alice')}")

# # Accessing a missing key without a default (returns None)
# print(f"Dave's score: {scores.get('Dave')}")

# Accessing a missing key with a specified default
# print(f"Eve's score: {scores.update("Bob",0)}")


# def generate(n) :
#   a = [[1],[1,1]]
#   if n ==1:
#     return [[1]]
#   elif n==2:
#     print( a)   
#   else:
#     if len(a)==n-1:
#       b=[0]*n
#       b[0] = b[-1] = 1
#       for i in range(1,n-1):
#         b[i] = a[-1][i]+a[-1][i-1]  
#       a.append(b)
#     generate(n-1) 
#     print (a)  
  
# print(generate(3))  


# def ai(n):
#   for i in range(n):
#     print('*')
# print(ai(5))