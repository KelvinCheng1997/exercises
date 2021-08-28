def Power_digit_sum(n):
    number = list(str(2 ** n))  # pow number and convert number  in string and  list
    result = [int(i) for i in number]  # convert number in int and
    return sum(result)  # sum list


print(Power_digit_sum(15))  # result 26
print(Power_digit_sum(1000))  # result 1366

testing = [i for i in range(0,10)]
print("The list: {}".format(testing))
print("Testing: {} {} {}".format(sum(testing), max(testing), min(testing)))