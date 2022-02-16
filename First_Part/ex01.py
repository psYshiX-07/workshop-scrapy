#!/usr/bin/env python3
##
## EPITECH PROJECT, 2022
## workshop-scrapy
## File description:
## ex01
##



if __name__ == "__main__":
    i = 1

    while i < 100:
        if i % 3 == 0 and i % 5 == 0:
            print("ThreeFive")
        elif i % 3 == 0:
            print("Three")
        elif i % 5 == 0:
            print("Five")
        else:
            print(i)
        i += 1
    exit(0)