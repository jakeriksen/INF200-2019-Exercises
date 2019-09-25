from ..comp_to_loop import squares_by_comp
from math import sqrt

def test_zero_input_yields_length_zero():
    assert len(squares_by_comp(0)) == 0

def test_one_input_yields_length_one():
    assert len(squares_by_comp(1)) == 0

def test_correct_number_of_outputs():
    assert len(squares_by_comp(0)) == 0
    assert len(squares_by_comp(1)) == 0
    assert len(squares_by_comp(2)) == 1

def is_square(x):
    return abs(sqrt(x) - int(sqrt(x))) < 1e-10

def test_squares_by_loop_produces_squares():
    for number in squares_by_comp(50):
        assert is_square(number)