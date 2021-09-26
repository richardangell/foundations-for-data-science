import pytest

import solutions
import answers


@pytest.mark.parametrize(
    "a,b,c,d", 
    [
        (1, 2, 3, 4), 
        (1, 1, 1, 1), 
        (4, 5, -10, 9),
        (9.5, 1.5, 9, -9)
    ]
)
def test_add_and_subtract(a, b, c, d):
    
    assert solutions.add_and_subtract(a, b, c, d) == answers.add_and_subtract(a, b, c, d), \
        f'expected; {answers.add_and_subtract(a, b, c, d)} but got; {solutions.add_and_subtract(a, b, c, d)}'


@pytest.mark.parametrize(
    "value", 
    [
        (-10),
        (-5),
        (-1.1),
        (0),
        (4),
        (9.9)
    ]
)
def test_square(value):
    
    assert solutions.square(value) == answers.square(value), \
        f'expected; {answers.square(value)} but got; {solutions.square(value)}'


@pytest.mark.parametrize(
    "value", 
    [
        (0.0001),
        (1),
        (2),
        (3),
        (29.9)
    ]
)
def test_log_10(value):
    
    assert solutions.log_10(value) == answers.log_10(value), \
        f'expected; {answers.log_10(value)} but got; {solutions.log_10(value)}'


@pytest.mark.parametrize(
    "l", 
    [
        [1],
        [1, 2, 3],
        [6, 10],
        [-10, 10],
        [-4, 0.125, 10, 50]
    ]
)
def test_sum_list(l):
    
    assert solutions.sum_list(l) == answers.sum_list(l), \
        f'expected; {answers.sum_list(l)} but got; {solutions.sum_list(l)}'

    
@pytest.mark.parametrize(
    "s", 
    [
        ("abcd"),
        ("a"),
        ("djdsjdsjkbdsj"),
        ("1"),
        ("1.11112"),
        (1),
        (1.0),
        (False),
        ([1, 2, 3]),
        ((1, 2, 3))
    ]
)
def test_check_string_type(s):
    
    if type(s) is str:

        result = solutions.check_string_type(s)

        assert result == 1, \
            f"expected; 1 but got; {result}"

    else:

        with pytest.raises(TypeError):

            solutions.check_string_type(s)


@pytest.mark.parametrize(
    "s", 
    [
        ("abcd"),
        ("a"),
        ("djdsjdsjkbdsjdjdj"),
        ("1"),
        ("1.1111299999999"),
    ]
)
def test_long_string(s):
    
    assert solutions.long_string(s) == answers.long_string(s), \
        f'expected; {answers.long_string(s)} but got; {solutions.long_string(s)}'


@pytest.mark.parametrize(
    "s1,s2", 
    [
        ("abcd", "a"),
        ("abcd", "ab"),
        ("abcd", "ad"),
        ("a", "a"),
        ("djdsjdsjkbdsjdjdj", "123"),
        ("djdsjdsjkbdsjdjdj", "jkbds"),
        ("123", "2"),
        ("1.1111299999999", "."),
        ("0.383", "a")
    ]
)
def test_string_contrains_substring(s1, s2):
    
    assert solutions.string_contrains_substring(s1, s2) == answers.string_contrains_substring(s1, s2), \
        f'expected; {answers.string_contrains_substring(s1, s2)} but got; {solutions.string_contrains_substring(s1, s2)}'


@pytest.mark.parametrize(
    "int_value,string_value", 
    [
        (1, "a"),
        (0, "ab"),
        (10, "ad"),
        (3, "abab")
    ]
)
def test_print_int_string(capsys, int_value, string_value):

    answers.print_int_string(int_value, string_value)

    captured = capsys.readouterr()

    if int_value > 0:

        expected_output = "\n".join([string_value] * int_value) + "\n"

    else:

        expected_output = ""

    assert captured.out == expected_output, \
        f'expected; {expected_output} but got; {captured.out}'

