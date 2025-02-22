# # Q: Count te numbers of even value between range 1 to 10
# # A:
# c=0
# for i in range(1,11):
#     if i%2==0:
#         c+=1
# print('Count =',c)

# # Q: Count odd numbers between 100 to 200
# # A:
# c=0
# for i in range(100,200):
#     if i%2!=0:
#         c+=1
# print('Count =',c)


# # Q: Count the even numbers between the range input by the user
# # A:
# n=int(input('Enter initial range:'))
# m=int(input('Enter final range:'))
# c=0
# for i in range(n,m+1):
#     if i%2==0:
#         c+=1
# print('Count =',c)


# # Q: Count the odd numbers between the range input by the user
# # A:
# n=int(input('Enter initial range:'))
# m=int(input('Enter final range:'))
# c=0
# for i in range(n,m+1):
#     if i%2==1:
#         c+=1
# print('Count =',c)


# # Q: Count the numbers which are divisible by 2 and 3 (range input by the user)
# # A:
# n=int(input('Enter initial range:'))
# m=int(input('Enter final range:'))
# c=0
# for i in range(n,m+1):
#     if i%2==0 and i%3==0:
#         c+=1
# print('Count =',c)


# # Q: Count the total even and odd numbers between the range input by the user
# # A:
n=int(input('Enter initial range:'))
m=int(input('Enter final range:'))
ec=0
oc=0
for i in range(n,m+1):
    if i%2==0:
        ec+=1
    else:
        oc+=1
print('Even Count =',ec)
print('Odd Count =',oc)