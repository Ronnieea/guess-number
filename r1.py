import random
r = random.randint(1, 100)
while True:
	num = input('請猜數字:')
	if r == num:
		input('終於猜對了!')
		break
	else:
		if r > num:
			input('比答案小')
		else:
			input('比答案大')