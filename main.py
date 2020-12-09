from helpers import *
import rle

def enter_RLE():
	try:
		linesofinput = int(input('How many lines of data will you enter: '))
	except ValueError:
		print('That is not a valid integer\n')
		return enter_RLE()
	if linesofinput <= 2:
		print('You must input more than 2 lines\n')
		return enter_RLE()

	data = input_data(linesofinput)
	for line in rle.decode(data):
		print(line)

	print('\n')


def display_ASCII_art():
	filename = './files/' + input('Please enter the name of the ASCII art file: ')
	try:
		with open(filename, 'r') as file:
			print('\n')
			# this is to get rid of extra newlines but preserve whitespace
			filestr = ''
			for line in file:
				filestr += line
			print(filestr)
	except FileNotFoundError:
		print('Error: File not found :(')
	
	print('\n')


def convert_to_ASCII_art():
	filename = './files/' + input('Please enter the filename for the encoded data: ')
	try:
		with open(filename, 'r') as file:
			print('\n')
			for line in rle.decode(file):
				print(line.strip())
	except FileNotFoundError:
		print('Error: File not found :(')
	print('\n')


def convert_to_RLE():
	artfilesize = 0
	encfilesize = 0
	diff = 0
	percent = 0
	artfilename = './files/' + input('Please enter the filename for the ASCII art: ')
	encfilename = './files/' + input('Please enter a filename for the destination: ')

	try:
		with open(artfilename, 'r') as artfile, open(encfilename, 'w+') as encfile:
			for line in artfile:
				encline = rle.encode_line(line)
				encfile.write(encline)
				artfilesize += len(line)
				encfilesize += len(encline)
	except FileNotFoundError:
		print('Error: File not found :(')
		return convert_to_RLE()

	diff = artfilesize - encfilesize
	percent = (encfilesize / artfilesize) * 100
	print('The encoded file has', diff, 'less characters')
	print('The encoded file is ' + str(percent) + '% the size of the original')


def main():
	options = [
		'Enter (RLE) encoded ASCII art',
		'Display ASCII art',
		'Convert to ASCII art',
		'Convert to RLE',
		'Quit'
	]
	choice = menu(options)
	if choice == 1:
		enter_RLE()
	elif choice == 2:
		display_ASCII_art()
	elif choice == 3:
		convert_to_ASCII_art()
	elif choice == 4:
		convert_to_RLE()
	else:
		print('Adios...')
		exit()


main()