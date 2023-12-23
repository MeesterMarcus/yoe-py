#!/usr/bin/env python3
import math

"""
Calculate total years of experience
"""

__author__ = "Marcus Lorenzana"
__version__ = "0.1.0"
__license__ = "MIT"


def main():
    # get total num of jobs
    jobs = int(input("Enter total number of jobs you've been at: "))
    yearsSum = 0
    monthsSum = 0
    # loop through jobs, retrieve yoe for each
    for x in range(jobs):
        years = int(input(f"Enter number of years at job {x + 1}: "))
        months = int(input(f"Enter number of months at job {x + 1}: "))
        yearsSum += years
        monthsSum += months
    # convert years to months for easier math
    yearsToMonths = yearsSum * 12
    # add all months together
    totalMonths = yearsToMonths + monthsSum
    # get total years by dividing by 12
    totalYearsExp = math.floor(totalMonths / 12)
    # get total months with modulo operator by 12
    totalMonthsExp = totalMonths % 12
    print(totalMonthsExp)
    print(f"Your total years of experience is: {totalYearsExp} yrs {totalMonthsExp} months")


if __name__ == "__main__":
    main()