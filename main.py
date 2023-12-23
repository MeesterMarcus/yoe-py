#!/usr/bin/env python3
import math

"""
Calculate total years of experience
"""

__author__ = "Marcus Lorenzana"
__version__ = "0.1.0"
__license__ = "MIT"


def main():
    jobs = int(input("Enter total number of jobs you've been at: "))
    yearsSum = 0
    monthsSum = 0
    for x in range(jobs):
        years = int(input(f"Enter number of years at job {x + 1}: "))
        months = int(input(f"Enter number of months at job {x + 1}: "))
        yearsSum += years
        monthsSum += months
    yearsToMonths = yearsSum * 12
    totalMonths = yearsToMonths + monthsSum
    totalYearsExp = math.floor(totalMonths / 12)
    totalMonthsExp = totalMonths % 12
    print(totalMonthsExp)
    print(f"Your total years of experience is: {totalYearsExp} yrs {totalMonthsExp} months")


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()