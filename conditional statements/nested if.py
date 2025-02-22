# An if statement inside another if statement known as nested if

# Syntax
# if(condition1):
#     if(condition2):
#         body of if
#     elif(condition3):
#         body of elif
# elif(condition4):
#     body of elif


# Q: Accept age,sex(M/F),number of days of work and display the wages accordingly
# Age                 Sex    Wage/day
# >=18 and <30        M      700
#                     F      750
# >=30 and <=40       M      800
#                     F      850
# A:
a=int(input('Age:'))
s=input('Gender:')
d=int(input('Number of days of work:'))
if(18<=a<30):
    if(s=='M'):
        print('Wage=',d*700)
    elif(s=='F'):
        print('Wage=',d*750)
elif(30<=a<=40):
    if (s=='M'):
        print('Wage=',d*800)
    elif(s=='F'):
        print('Wage=',d*850)
else:
    print('Invalid')
