# lst=[2,3,4,5,6]

# cubes=[n**3 for n in lst ]
# print(cubes)

# add_two=[n+2 for n in lst ]
# print(add_two)

# numgt=[n for n in lst if n>5]
# print(numgt)

# evens=[n for n in lst if n%2==0]
# print(evens)

# odds=[n for n in lst if n%2!=0]
# print(odds)

years=[y for y in range(1800,2026)]
# century_years=[y for y in years if y%100==0]
# print(century_years)

non_century=[y for y in years if y%100!=0]
print(non_century)
