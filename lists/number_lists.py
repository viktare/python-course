numbers = range(1, 1000000)
# print(min(numbers))
# print(max(numbers))
# print(sum(numbers))

odd_numbers = range(1, 21, 2)
for odd in odd_numbers:
    print(odd)

print('========================================')

threes = range(3, 31, 3)
for three in threes:
    print(three)

print('========================================')

cubes = range(1, 11)
for cube in cubes:
    print(cube**3)

print('========================================')

results = [comp**3 for comp in range(1, 11)]
print(results)
    