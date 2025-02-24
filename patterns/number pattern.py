# # Q: 1
# #    2 2
# #    3 3 3
# #    4 4 4 4
# #    5 5 5 5 5
# # A:
# for i in range(5):
#     for j in range(i+1):
#         print(i+1,end=' ')
#     print()


# # Q: 1 1 1 1
# #    2 2 2
# #    3 3
# #    4
# # A:
# for i in range(4):
#     for j in range(4-i):
#         print(i+1,end=' ')
#     print()


# # Q: 4
# #    3 3
# #    2 2 2
# #    1 1 1 1
# # A:
# for i in range(4):
#     for j in range(i+1):
#         print(4-i,end=' ')
#     print()


# # Q: 1
# #    1 2
# #    1 2 3
# #    1 2 3 4
# #    1 2 3 4 5
# # A:
# for i in range(5):
#     for j in range(i+1):
#         print(j+1,end=' ')
#     print()
#
# # Note:
# #-------
# # i = 0:
# # Inner loop: for j in range(0 + 1) (which is range(1)).
# # j takes the value 0.
# # print(0 + 1, end=' ') prints "1 ".
# # print() moves to the next line.
# # Output: 1
# # i = 1:
# #
# # Inner loop: for j in range(1 + 1) (which is range(2)).
# # j takes the values 0 and 1.
# # print(0 + 1, end=' ') prints "1 ".
# # print(1 + 1, end=' ') prints "2 ".
# # print() moves to the next line.
# # Output: 1 2


# # Q:1 2 3 4 5
# #   1 2 3 4
# #   1 2 3
# #   1 2
# #   1
# # A:
# for i in range(5):
#     for j in range(5-i):
#         print(j+1,end=' ')
#     print()


# # Q:   1
# #    2   2
# # 3    3    3
# #    2    2
# #      1
# # A:
# for i in range(3):
#     for k in range(2-i):
#         print(' ',end=' ')
#     for j in range(i+1):
#         print(i+1,end='   ')
#     print()
# for i in range(2):
#     for k in range(i+1):
#         print(' ',end=' ')
#     for j in range(2-i):
#         print(2-i,end='   ')
#     print()