import re
# word=input('Enter a word:')
# # rule='[A-Z]+'
# rule='[A-Za-z\s]+'  # uppercase, lowercase and space
# match=re.fullmatch(rule,word)
# if match:
#     print('Valid')
# else:
#     print('Invalid')


# # Name validation with space.
# # it should start with capital letter followed by small letter. limit of letters is 8 to 10
#
# name=input('Enter your name:')
# rule='[A-Z][a-z]{7,9}'    # first letter selects from [A-Z] rest 7 to 9 letters will be from [a,b]
# match=re.fullmatch(rule,name)
# if match:
#     print('Valid')
# else:
#     print('Invalid')


# # Phone number validation.
# # should starts with country code +91
# # start with 9,8,7 or 6
# # 10 numbers
#
# phone=input('Enter your phone number:')
# rule='[+][9][1][6-9][0-9]{9}'
# match=re.fullmatch(rule,phone)
# if match:
#     print('Valid Phone Number')
# else:
#     print('Invalid Phone Number')


# # ID validation
# # valid - alphabets only , alphabets with two digits in the end
# # Invalid - alphabets with 1 or more than 2 digits
#
# n=input('Enter your ID:')
# rule='[a-z]+|[a-z]+[0-9]{2}'
# match=re.fullmatch(rule,n)
# if match:
#     print('Valid')
# else:
#     print('Invalid')


# # Date validation
#
# n = input('Input:')
# rule='([1-9]|0[1-9]|1[0-9]|2[0-9][3][0-1])[-]([1-9]|0[1-9]|1[0-2])[-][1-9][0-9]{3}'
# match=re.fullmatch(rule,n)
# if match:
#     print('Valid')
# else:
#     print('Invalid')


# # Gmail validation
#
# n = input('Input:')
# rule='([a-z]+[0-9._-]+|[a-z._-]+[0-9]+[a-z._-]+@gmail.com)'
# match=re.fullmatch(rule,n)
# if match:
#     print('Valid')
# else:
#     print('Invalid')


# regexlib.com - site for find regex patterns that match common data formats