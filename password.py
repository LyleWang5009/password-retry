password = 'a123456'
i = 3
while password == 'a123456':
	pwd = input('enter your password: ')
	if pwd == password:
		print ('Log in success')
		break
	else:
		i = i - 1
		print('Log in failed', i,'more times')
		if i == 0:
			break