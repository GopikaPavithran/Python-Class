# # Q: A
# #    B B
# #    C C C
# # A:
# for i in range(65,68):
#     for j in range(i-64):
#         print(chr(i),end=' ')
#     print()


# # Q: a
# #    b b
# #    c c c
# # A:
# for i in range(97,100):
#     for j in range(i-96):
#         print(chr(i),end=' ')
#     print()


# # Q: c c c
# #    b b
# #    a
# # A:
# for i in range(99,96,-1):
#     for j in range(i-96):
#         print(chr(i),end=' ')
#     print()


# # Q: a a a
# #    b b
# #    c
# # A:
# for i in range(97,100):
#     for j in range(100-i):
#         print(chr(i),end=' ')
#     print()


# # Q: A
# #    A B
# #    A B C
# # A:
# for i in range(65,68):
#     for j in range(i-64):
#         print(chr(j+65),end=' ')
#     print()


# # Q:   a
# #    b b
# #  c c c
# # A:
# for i in range(97,100):
#     for k in range(99-i):
#         print(' ',end=' ')
#     for j in range(i-96):
#         print(chr(i),end=' ')
#     print()


# # Q:   A
# #    B B
# #  C C C
# # A:
# for i in range(65,68):
#     for k in range(67-i):
#         print(' ',end=' ')
#     for j in range(i-64):
#         print(chr(i),end=' ')
#     print()


# Q:   A
#    B B
#  C C C
#    B B
#      A
# A:
for i in range(65,68):
    for k in range(67-i):
        print(' ',end=' ')
    for j in range(i-64):
        print(chr(i),end=' ')
    print()
for i in range(66,64,-1):
    for k in range(67-i):
        print(' ',end=' ')
    for j in range(i-64):
        print(chr(i),end=' ')
    print()