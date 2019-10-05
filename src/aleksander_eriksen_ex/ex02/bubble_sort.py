def bubble_sort(data_):
	"""
	This takes in a "tuple", then makes a new list.
	Then it runs through the row,
	then swapping the place of the number,
	if it is less than the one in front.
	This way the smaller numbers get pushed back,
	while the larger get pushed forward.

	Parameters
	----------
	data_

	Returns
	-------
	new_list

	"""

	length = len(data_)
	sort_li = list(data_)
	for row in range(length - 1):
		for number in range(length - 1 - row):
			if sort_li[row] > sort_li[row + 1]:
				sort_li[row], sort_li[row + 1] = sort_li[row + 1], sort_li[
                    row]
	return sort_li


if __name__ == "__main__":

	for data in ((),
				 (1,),
				 (1, 3, 8, 12),
				 (12, 8, 3, 1),
				 (8, 3, 12, 1)):
		print('{!s:>15} --> {!s:>15}'.format(data, bubble_sort(data)))
