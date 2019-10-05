# -*- coding: utf-8 -*-

__author__ = 'Aleksander Eriksen'
__email__ = 'jaer@nmbu.no'

import numpy as np
import pytest


def median(data):
	"""
	Returns median of data.

	:param data: An iterable of containing numbers
	:return: Median of data
	"""

	sorted_data = sorted(data)
	num_elements = len(sorted_data)
	if not num_elements % 2 != 1:
		return sorted_data[num_elements // 2]
	elif not sorted_data:
		raise ValueError('Insert a list containing numbers!')
	else:
		return (sorted_data[num_elements // 2 - 1]
				+ sorted_data[num_elements // 2]) / 2


def test_median_singleton():
	"""Checks if the median of a single element list is the singleton
	"""
	assert median([4]) == 4


def is_odd(number):
	"""Takes a number and checks if it's odd
	"""
	if not number % 2 == 1:
		return False
	return True


def test_median_odd():
	"""Checks if the number given is odd, from an odd list
	Then control-checks with numpy"""
	data = [1, 3, 5, 7, 9]
	assert is_odd(median(data)) is True
	assert median(data) == np.median(data)


def is_even(number):
	"""Takes a number and checks if it is even
	"""
	if not number % 2 == 0:
		return False
	return True


def test_median_even():
	"""Checks if the number given is even, from an even list
	Then control-checks with numpy
	"""
	data = [2, 4, 6, 8, 10]
	assert is_even(median(data)) is True
	assert median(data) == np.median(data)


def test_median_ordered():
	"""Test on a ordered list, and control-checks with numpy
	"""
	data = [0, 1, 2, 3, 4, 5, 6, 7]
	assert median(data) == np.median(data)


def test_median_reversed():
	"""Testing the function with an unordered list, and checks with numpy
	"""
	data = [8, 7, 6, 5, 4, 3, 2, 1]
	assert median(data) == np.median(data)


def test_median_unordered():
	"""Test on a unordered list, and control-checks with numpy"""
	data = [8, 3, 5, 7, 2, 1]
	assert median(data) == np.median(data)


def test_median_raises_value_error_on_empty_list():
	"""If a empty list occurs, a value error raises
	"""
	with pytest.raises(ValueError):
		median([])


def test_original_unchanged():
	"""Checks if the data is unchanged after using function
	"""
	data = [1, 2, 3, 4, 5, 6]
	median(data)
	assert data == [1, 2, 3, 4, 5, 6]


def test_median_tuple():
	"""Tests if a tuple and a list gives the same output
	"""
	list_ = [1, 2, 3, 4, 5, 6]
	tuple_ = tuple(list_)
	assert median(tuple_) == median(list_)
