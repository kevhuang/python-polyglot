x = 20

if x > 18: 
  print('x is greater than 18')
elif x % 4 == 0:
  print('x is divisible by 4')
else:
  print('fruit')


if True:
  print('this is true')

if not True:
  print('this is curiously true')
  print(~~False)
else:
  print('this is not true')


if True and False:
  print('True and False')
elif True or False:
  print('True or False')


y = [1,5,17]

if 17 in y and 2 not in y:
  print('all is well')