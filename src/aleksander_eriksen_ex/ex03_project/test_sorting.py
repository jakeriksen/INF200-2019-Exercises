# -*- coding: utf-8 -*-

__author__ = 'Aleksander Eriksen'
__email__ = 'jaer@nmbu.no'

import random
import string

import pytest


@pytest.fixture  # Decorator for the functions
def data_list():  # Gives a given list of data
	return [3, 2, 1]


def bubble_sort(data):
	length = len(data)
	array = list(data)
	while True:
		corrected = False
		for row in range(length - 1):
			if array[row] > array[row + 1]:
				array[row], array[row + 1] = array[row + 1], array[row]
				corrected = True
		if not corrected:
			return array


def test_empty():
	"""Test that the sorting function works for empty list
	"""
	empty = []
	assert bubble_sort(empty) == []


def test_single():
	"""Test that the sorting function works for single-element list
	"""

	single = [1]
	assert bubble_sort(single) == [1]


def test_sorted_is_not_original(data_list):
	"""
	Test that the sorting function returns a new object.

	Consider

	data = [3, 2, 1]
	sorted_data = bubble_sort(data)

	Now sorted_data shall be a different object than data,
	not just another name for the same object.
	"""

	sorted_data = bubble_sort(data_list)
	assert sorted_data is not data_list


def test_original_unchanged(data_list):
	"""
	Test that sorting leaves the original data unchanged.

	Consider

	data = [3, 2, 1]
	sorted_data = bubble_sort(data)

	Now data shall still contain [3, 2, 1].
	"""

	old_data = data_list
	sorted_data = bubble_sort(data_list)

	assert old_data == data_list
	assert sorted_data is not old_data


def test_sort_sorted():
	"""Test that sorting works on sorted data.
	"""
	data = [1, 2, 3, 4, 5]
	sorted_data = bubble_sort(data)
	assert sorted_data == data


def test_sort_reversed():
	"""Test that sorting works on reverse-sorted data.
	"""
	data = [5, 4, 3, 2, 1]
	sorted_data = bubble_sort(data)
	sorted_data.reverse()
	assert sorted_data == data


def test_sort_all_equal():
	"""Test that sorting handles data with identical elements.
	"""
	equal_6_ones = [1] * 6
	sorted_ones = bubble_sort(equal_6_ones)
	assert sorted_ones == equal_6_ones


def is_sorted(sorted_list):
	"""Checks if a list is sorted, by comparing two numbers in iteration
	"""
	for small, large in zip(sorted_list[:-1], sorted_list[1:]):
		if small > large:
			return False
	return True


def random_digit_str_list():
	"""Gives a list with random digits (0-9) in string form
	"""
	return [random.choice(string.digits)
			for _ in range(random.randint(1, 20))]


def random_ascii_str_list():
	"""Gives a list with random ascii letters (str), random length
	"""
	return [random.choice(string.ascii_letters)
			for _ in range(random.randint(1, 20))]


def random_float_list():
	"""Gives a random float list, with random length
	"""
	return [random.uniform(0, 10) for _ in range(1, 20)]


def random_int_list():
	"""Gives a list with random number in a given range, with random length
	"""
	return [random.randint(0, 10) for _ in range(1, 20)]


def test_sorting():
	"""
	Test sorting for various test cases.

	This test case should test sorting of a range of data sets and
	ensure that they are sorted correctly. These could be lists of
	numbers of different length or lists of strings.
	"""

	# Test for a random list with integers
	int_list = random_int_list()
	sorted_int = bubble_sort(int_list)

	assert sorted_int == sorted(int_list)
	assert len(sorted_int) == len(int_list)
	assert is_sorted(sorted_int) is True

	# Test for a random float list
	float_list = random_float_list()
	sorted_float = bubble_sort(float_list)

	assert sorted_float == sorted(float_list)
	assert len(sorted_float) == len(float_list)
	assert is_sorted(sorted_float) is True

	# Test for random ascii letters (str) in list
	ascii_list = random_ascii_str_list()
	sorted_ascii = bubble_sort(ascii_list)

	assert sorted_ascii == sorted(ascii_list)
	assert len(sorted_ascii) == len(ascii_list)
	assert is_sorted(sorted_ascii) is True

	# Test for random digits as string in list
	digit_str_list = random_digit_str_list()
	sorted_digit_str = bubble_sort(digit_str_list)

	assert sorted_digit_str == sorted(digit_str_list)
	assert len(sorted_digit_str) == len(digit_str_list)
	assert is_sorted(sorted_digit_str) is True
