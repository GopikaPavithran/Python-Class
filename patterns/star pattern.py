# # Q: Right Triangle
# #   *
# #   * *
# #   * * *
# # A:
# for i in range(1,4):
#     for j in range(i):
#         print('*',end=' ')
#     print()


# # Q: square
# #   *  *  *
# #   *  *  *
# #   *  *  *
# # A:
# for i in range(3):
#     for j in range(3):
#         print('*',end='  ')
#     print()


# # Q: * * *
# #    * *
# #    *
# # A:
# for i in range(3):
#     for j in range(3-i):
#         print('*',end=' ')
#     print()


# # Q: *
# #    * *
# #    * * *
# #    * * * *
# #    * * *
# #    * *
# #    *
# # A:
# for i in range(1,5):
#     for j in range(i):
#         print('*',end=' ')
#     print()
# for i in range(3):
#     for j in range(3-i):
#         print('*',end=' ')
#     print()


# # Q:  *
# #   *   *
# # *   *   *
# # A:
# for i in range(1,4):
#     for k in range(3-i):
#         print(' ',end=' ')
#     for j in range(i):
#         print('*',end='   ')
#     print()


# # Q: *   *   *
# #      *   *
# #        *
# # A:
# for i in range(3):
#     for k in range(i):
#         print(' ',end=' ')
#     for j in range(3-i):
#         print('*',end='   ')
#     print()


# # Q:    *
# #     * *
# #   * * *
# # A:
# for i in range(1,4):
#     for k in range(3-i):
#         print(' ',end=' ')
#     for j in range(i):
#         print('*',end=' ')
#     print()


# # Q: * * *
# #      * *
# #        *
# # A:
# for i in range(3):
#     for k in range(i):
#         print(' ',end=' ')
#     for j in range(3-i):
#         print('*',end=' ')
#     print()