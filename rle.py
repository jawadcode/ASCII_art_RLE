# RLE encoding and decoding functions

import textwrap

def join_pair(count, char):
	countstr = str(count)
	fmtcountstr = '0' + countstr if len(countstr) == 1 else countstr
	return fmtcountstr + char


def encode_line(line):
	char = ''
	count = 0
	res = ''
	for i in range(len(line)):
		if i == 0:
			char = line[i]
			continue
		elif i == len(line) - 1:
			res += join_pair(count, char)
			if char == line[i]:
				count += 1
			else:
				char = line[i]
				count = 1
			res += join_pair(count, char)
		else:
			if char == line[i]:
				count += 1
			else:
				res += join_pair(count, char)
				char = line[i]
				count = 1

	return res
		

def encode(data):
	for line in data:
		yield encode_line(line)
	
	return


def decode(data):
	for line in data:
		pairs = [line[i:i+3] for i in range(0, len(line), 3)]
		res = ''
		for pair in pairs:
			if '\n' in pair:
				res += '\n'
			else:
				try:
					count = int(pair[0:2])
				except ValueError:
					return ""
				char = pair[2]
				res += char * count
		
		yield res
	
	return