import random

def num_digits(num):
    count = 0
    while num > 0:
        count += 1
        num //= 10
    return count

def sum_of_digits(num):
    total = 0
    while num > 0:
        remainder = num % 10
        total += remainder
        num //= 10
    return total

def cd_keygen():
    x1 = random.randint(0, 1000)
    while x1 % 111 == 0:
        x1 = random.randint(0, 1000)
    x1_str = ""
    if x1 > 100:
        x1_str = str(x1)
    if 10 < x1 < 100:
        x1_str = "0" + str(x1)
    if x1 < 10:
        x1_str = "00" + str(x1)
    x2 = 1
    while sum_of_digits(x2) % 7 != 0:
        x2 = random.randint(0, 10000000)
        while x2 % 10 == 0 or x2 % 10 == 8 or x2 % 10 == 9:
            x2 = random.randint(0, 10000000)
    length = num_digits(x2)
    x2_str = ""
    for i in range(0, 7 - length):
        x2_str += "0"
    x2_str += str(x2)
    return x1_str + "-" + x2_str

def oem_keygen():
    doy = random.randint(1, 367)
    length = num_digits(doy)
    doy_str = ""
    for i in range(0, 3 - length):
        doy_str += "0"
    doy_str += str(doy)
    year_str = random.choice(["95", "96", "97", "98", "99", "00", "01", "02", "03"])
    x2 = 1
    x2_str = "0"
    while sum_of_digits(x2) % 7 != 0:
        x2 = random.randint(0, 1000000)
        while x2 % 10 == 0 or x2 % 10 == 8 or x2 % 10 == 9:
            x2 = random.randint(0, 1000000)
    length = num_digits(x2)
    for i in range(0, 6 - length):
        x2_str += "0"
    x2_str += str(x2)
    x3 = random.randint(0, 100000)
    x3_str = ""
    for i in range(0, 5 - length):
        x3_str += "0"
    x3_str += str(x3)
    return doy_str + year_str + "-OEM-" + x2_str + "-" + x3_str
