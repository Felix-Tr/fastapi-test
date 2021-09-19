import math


def int2str(number: int):
    """
    Converts number into string, e.g. 125 => One hundred and twenty-five,
    the routine increments order by order to generate the final string
    :param number: int
    :return: number_string: string
    """

    if number == 0:
        return 'Zero'
    number_string = []
    number = [int(n) for n in reversed(str(number))]
    for i, n in enumerate(number):
        n_bef = number[i-1]
        if i in [2, 5]:
            # Include hundred, and if necessary
            if n_bef != 0 or number[i-2] != 0:
                number_string.append("and")
            if n != 0:
                number_string.append("hundred")
        elif i in [1, 4]:
            # Format second order words
            if n == 1 and 1 <= n_bef <= 9:
                # special case 11-19
                del number_string[-1]
                number_string.append(numbers[n*10 + n_bef])
                continue
            else:
                if n > 0:
                    if n_bef !=0:
                        # normal case X1-X9
                        number_string.append(numbers[n*10] + "-" + number_string.pop())
                    else:
                        number_string.append(numbers[n*10])
                    continue
        if i == 3:
            number_string.append("thousand")
        if n != 0:
            number_string.append(numbers[n])

    number_string = " ".join(list(reversed(number_string)))
    number_string = number_string[0].upper() + number_string[1:]
    return number_string


numbers = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
           11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen",
           19: "nineteen", 20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty", 70: "seventy",
           80: "eighty", 90: "ninety"}

# if __name__ == '__main__':
#
#     print(0, " ", int2str(0))
#     print(1, " ", int2str(1))
#     print(12, " ", int2str(12))
#     print(25, " ", int2str(25))
#     print(103, " ", int2str(103))
#     print(814, " ", int2str(814))
#     print(1201, " ", int2str(1201))
#     print(201410, " ", int2str(201410))