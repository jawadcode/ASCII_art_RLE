# some miscellaneous functions

def menu(options):
	fmtoptions = ''.join(['\n\t' + str(i + 1) + '. ' + options[i] for i in range(len(options))])
	print('Please pick a number:', fmtoptions)
	try:
		option = int(input('=> '))
	except ValueError:
		print('That is not a valid integer.\n')
		return menu(options)
	if option in range(len(options)):
		return option
	else:
		print(option, 'is not an option')
		return menu(options)


def display(data):
	for line in data:
		print(line.strip())


def input_data(linecount):
	return [input(str(i) + '. ') for i in range(linecount)]