def high_and_low(numbers: str):
    numbers_list = []
    for number in set(numbers.split()):
        numbers_list.append(int(number))
    return f"{max(numbers_list)} {min(numbers_list)}"

numbers = "-13 80 95 -13 14 31 35 67 -57 53 96 -27 72 99 -23 23 68";
print(high_and_low(numbers))