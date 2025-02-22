# # Q: Find sum of 10 natural numbers
# # A:
# sum=0
# for i in range(1,11):
#     sum+=i
# print('Sum =',sum)


# # Q: Find sum of even numbers fall between the range (100,200)
# # A:
# s=0
# for i in range(100,200):
#     if i%2==0:
#         s+=i
# print('Sum=',s)


# # Q: Sum of first 10 odd numbers
# # A:
# s=0
# for i in range(1,20):
#     if i%2!=0:
#         s+=i
# print('Sum=',s)


# Q: display sum of both odd and even numbers that fall between 12 and 37
# A:
odd_s=0
even_s=0
for i in range(13,37):
    if i%2==0:
        even_s+=i
    elif i%2!=0:
        odd_s+=i
print('Sum of odd numbers =',odd_s)
print('Sum of even numbers =',even_s)