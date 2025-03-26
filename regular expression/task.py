# import re
#
# print('Registration Page\n-----------------')
# u=input('Username:')
# e=input('Email:')
# p=input('Phone:')
# pas=input('Password:')
# con=input('Confirm password:')
# r1='^[a-z0-9._-]{3,16}$'      # ^ and $ characters are anchors for beginning and end of regex pattern respectively
# r2='[a-z0-9._-]+@gmail.com'
# r3='[+][9][1][6-9][0-9]{9}'
# r4='(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^&*]).{8,}'
#                                 # (?=.*)is a positive lookahead assertion in regular expressions.
#                                 # (?=...): This is the syntax for a positive lookahead. It means "assert that what follows the current
#                                                     # position in the string matches the pattern inside the parentheses, but don't include
#                                                     # that match in the overall result."
#                                 # .: This matches any character (except newline, unless you use the s flag).
#                                 # *: This is a quantifier meaning "zero or more occurrences" of the preceding element.
#                                 # Putting it together, (?=.*) means: Assert that anywhere after the current position in the string, there is
#                                                                                                             # zero or more of any character.
# match1=re.fullmatch(r1,u)
# match2=re.fullmatch(r2,e)
# match3=re.fullmatch(r3,p)
# match4=re.fullmatch(r4,pas)
# if match1 and match2 and match3 and match4:
#     if pas==con:
#         print('Registration Completed.')
#         print('Login Page\n--------')
#         us=input('Username:')
#         pa=input('Password:')
#         if us==u and pa==pas:
#             print('Welcome')
#         else:
#             print('Incorrect username or password')
#     else:
#         print('Password is not matching')
# else:
#     print('Registration failed. Please input valid data')



                         # This program is not working properly.Need to rewrite!