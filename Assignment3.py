#Q1
lst = [1,2,3,4,5]
#Sum Method 1
print("Sum Methods\nM1 :",sum(lst))
sum = 0
#Sum Method 2
for x  in lst:
    sum=sum+x
print("M2 :",sum)


#Q2
# Concatination Method 1
lst2=[5,6,7,8,9]
lst3=lst+lst2
print("Concatination Methods\nM1 :",lst3)
# concatination method 2
lst.extend(lst2)
print("M2 :",lst)


#Q3
# finding element is present or not 
# M1
print("Elements exiistence\nM1 = ",10 in lst)
# M2 learned from Hackers_Rank
print("M2 = ",any(x == 2 for x in lst))


#Q4
# Removing duplicates
#M1
temp = []
for x in lst:
    if x not in temp:
        temp.append(x)
lst=temp
print("List with duplicates removed:", lst)
# #M2 DSA way
# lst.append(1)
# lst.append(2)
# lst.append(3)
# lst.append(10)
# #concept of sclection sort
# # Got from GPT
# n = len(lst)
# for i in range(n):
#     j = i + 1
#     while j < n:
#         if lst[j] == lst[i]:
#             lst.pop(j)
#             n -= 1
#         else:
#             j += 1
# print(lst)         
# 
# #M3 remove duplicate from sorted array
# # we can use bubble sort



#Q5
#numpy 
import numpy as np
arr  = np.array(lst)
# mean 
print("Numpy functions\nMean  = ",np.mean(lst))
# median
print("Median= ",np.median(lst))
# std
print("STD   = ",np.std(lst))