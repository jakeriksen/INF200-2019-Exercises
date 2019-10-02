# -*- coding: utf-8 -*-

__author__ = 'Aleksander Eriksen'
__email__ = 'jaer@nmbu.no'

import pytest


@pytest.fixture # Decorator for the functions
def data_list(): # Gives a given list of data
	return [3, 2, 1]


def bubble_sort(data):

	length = len(data)
	sort_li = list(data)
	for row in range(length - 1):
		for number in range(length - 1 - row):
			if sort_li[row] > sort_li[row + 1]:
				sort_li[row], sort_li[row + 1] = sort_li[row + 1], sort_li[row]

	return sort_li


def test_empty():
		"""Test that the sorting function works for empty list
		"""

		with pytest.raises(ValueError)
			bubble_sort([])
		pass

def test_single():
		"""Test that the sorting function works for single-element list"""

		single = [1]
		assert bubble_sort(single)





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
		# BEFORE PULLING: check if not misunderstood; object != type()
		assert sorted_data != data_list

def test_original_unchanged(data_list):
		"""
		Test that sorting leaves the original data unchanged.

		Consider

		data = [3, 2, 1]
		sorted_data = bubble_sort(data)

		Now data shall still contain [3, 2, 1].
		"""

		old_data = data_list
		sorted_data = bubble_sort(data_list) # If even necessary
		# Maybe make if statements that returns bool

		# OR: (?)
		# old_data = [3, 2, 1]
		assert old_data == data_list


def is_sorted(iterable):
	for small, large in zip(sorted_list[:-1], sorted_list[1:]):
		if small > large:
			return False
	return True


def test_sort_sorted():
		"""Test that sorting works on sorted data."""

		pass

def test_sort_reversed():
		"""Test that sorting works on reverse-sorted data."""
		pass

def test_sort_all_equal():
		"""Test that sorting handles data with identical elements."""
		pass

def test_sorting():
		"""
		Test sorting for various test cases.

		This test case should test sorting of a range of data sets and
		ensure that they are sorted correctly. These could be lists of
		numbers of different length or lists of strings.
		"""
		pass