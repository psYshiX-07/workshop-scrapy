##
## EPITECH PROJECT, 2022
## workshop-scrapy
## File description:
## ex03
##

if __name__ == "__main__":
    i = 0
    res = 0
    test = ['4', '3', '-2']

    if len(test) == 1:
        print("calculate(", test, ") -> False")
    for i in range(len(test)):
        if test[i][0] == '-' and test[i][1].isdigit():
            res += int(test[i])
        elif test[i].isdigit():
            res += int(test[i])
    print("calculate(", test, ") -> ", res)
    exit(0)