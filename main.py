# SOFTWARE ENGINEERING & TESTING - OBLIGATORY ASSIGNMENT 2: TESTING


"""
A year is considered a leap year as long as the following conditions are met:

* The year IS dividable by 4 BUT NOT 100
** The year IS dividable by 400

A year IS NOT considered a leap year as long as the following conditions are met:

* The year IS NOT dividable by 4
** The year IS dividable by 100 BUT NOT 400
"""


def is_leap_year(year: int):
    if year % 4 == 0 and 100 != 0:
        print("Condition 1 - leap year")
        return True

    if year % 400 == 0:
        print("Condition 2 - leap year")
        return True

    elif year % 4 != 0:
        print("Condition 3 - NOT leap year")
        return False

    if year % 100 == 0 and 400 != 0:
        print("Condition 4 - NOT leap year")
        return False

# Adding a comment - pushing to remote, hopefully triggering workflow.
