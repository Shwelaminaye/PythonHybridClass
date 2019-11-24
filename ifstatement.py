# x = int(input("please enter an int" ))
# if x < 5:
# 	x = 0
# 	print('x is smaller than 5')
# elif x > 10:
# 	print('x is bigger than 10')
# elif x == 7:
# 	print('x is 7')
# elif x > 5 and x < 10:
# 	print('x is between 5 and 10')
# else:
# 	print('x is undefined')

x = int(input("please enter an age"))
if x > 75:
	x = 0
	print('go to anywhere')
elif x > 0 and x <= 18:
	print('go to school')
elif x >= 19 and x < 51:
	print('go to trip')
elif x > 50 and x < 76:
	print('go to monestry')
else:
	print(''i told that "I don't like it"'')

words = ['cat', 'window', 'defenstrate']
for w in words:
	print(w, len(w))

fruits = ['apple','banana','cucumber','pineapple','orange']
for f in fruits:
	print(f, len(f))

for i in range(5):
	print(i)

	