def char_counts(textfilename):
	"""
	The char_counts() function opens the file with the given filename
	using encoding utf-8
	and reads the entire file content into a single string.
	It then counts each character code (0–255) that occurs in the string
	and returns the result as a list,
	result[i] gives the number of occurances of charactor (ascii) code [i].

	Parameters
	----------
	textfilename

	Returns
	-------
	"""

	with open(textfilename, 'r', encoding='utf-8') as file:
		characters = [char for char in file.read()]
		result = [0] * 256
		for i in range(256):
			for char in characters:
				ascii_code = ord(char)
				if ascii_code == i:
					result[ascii_code] += 1

	return result


if __name__ == '__main__':

	filename = 'file_stats.py'
	frequencies = char_counts(filename)
	for code_ascii in range(256):
		if frequencies[code_ascii] > 0:
			character = ''
			if code_ascii >= 32:
				character = chr(code_ascii)

			print(
				'{:3}{:>4}{:6}'.format(
					code_ascii, character, frequencies[code_ascii]
				)
			)
