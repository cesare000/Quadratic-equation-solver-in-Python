import math


def pura():
	n = int(input('n: '))
	if n < 0:
		print('The equation is impossible')
	else:
		x_1 = math.sqrt(n)
		x_2 = math.sqrt(n) * (-1)
		print(f'x1= {x_1}, x2 = {x_2}')


def spuria():
	a = int(input('a: '))
	b = int(input('b: '))
	x_1 = 0
	x_2 = (b * (-1)/a) 
	print(f'x1= {x_1}, x2 = {x_2}')


def quadratic_formula():
	a = int(input('a: '))
	b = int(input('b: '))
	c = int(input('c: '))
	delta = (b**2 - 4*a*c)

	

	if delta < 0:
		print('The equation is impossible')
	else:	
		x_1 = (-b + math.sqrt(delta))/(2 * a)
		x_2 = (-b - math.sqrt(delta))/(2 * a)

		print(f'x1= {x_1}, x2 = {x_2}')


while True:
	equation_type = int(input('''Which is your equation?
	1) x**2 = n
	2) ax**2 + bx = 0
	3) ax**2 + bx + c = 0
	Type in the number of your equation: '''))


	if equation_type == 1:
		pura()
	elif equation_type == 2:
		spuria()
	elif equation_type == 3:
		quadratic_formula()

	choice = str(input('Do you want me to solve a new equation for you? [y/n]'))

	if choice == "n":
		break
	elif choice == "y":
		True




	





