##
## EPITECH PROJECT, 2022
## workshop-scrapy
## File description:
## ex02
##

from sys import argv

if __name__ == "__main__":
    a = 0
    b = 0
    final = 1
    res = [int(i) for i in argv[1]]
    lenght = len(res)
    new = []

    for a in range(lenght - 1):
        new.append(res[a] * res[a+1])

    while b < lenght:
        final *= res[b]
        b += 1
    new.append(final)

    a = 0
    b = 0
    for a in range(lenght):
        b = 0
        for b in range(lenght):
            if new[a] == res[b]:
                print(argv[1], "\t-->\tfalse")
                exit(84)
    print(argv[1], "\t-->\ttrue")
    exit(0)