# SOFTWARE ENGINEERING & TESTING - OBLIGATORY ASSIGNMENT 2: TESTING


from main import is_leap_year


# CHECKING IF SELECTED YEARS ARE VALID LEAP YEARS :
def test_division_allowed_by_four_and_not_hundred():
    assert is_leap_year(2000)
    assert is_leap_year(2004)
    assert is_leap_year(2024)


def test_division_allowed_by_four_hundred():
    assert is_leap_year(2000)
    assert is_leap_year(2004)
    assert is_leap_year(2024)


# CHECKING IF SELECTED YEARS ARE INVALID LEAP YEARS :
def test_division_not_allowed_by_four():
    assert is_leap_year(2001) is False
    assert is_leap_year(2003) is False
    assert is_leap_year(2006) is False


def test_division_allowed_by_hundred_and_not_four_hundred():
    assert is_leap_year(2001) is False
    assert is_leap_year(2003) is False
    assert is_leap_year(2006) is True
