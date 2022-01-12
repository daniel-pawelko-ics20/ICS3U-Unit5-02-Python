#!/usr/bin/env python3

# Created by: Daniel Pawelko
# Created on: Jan 2022
# Functions with parameters and what not


def area(length: float, height: float):
    # function to calculate area of triangle

    # process
    area = (length * height) / 2

    # output
    print("")
    print(f"The area of the triangle is {round(area, 2)} cm²")


def main():
    # main function for function with parameters program

    # input
    try:
        length = input("Enter the base length of a triangle (cm): ")
        length = float(length)
        height = input("Enter the height of a triangle (cm): ")
        height = float(height)
        # calling area function
        area(length, height)
    except:
        print("Please input a number")

    # done
    print("")
    print("Done.")


if __name__ == "__main__":
    main()
