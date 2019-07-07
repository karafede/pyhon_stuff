
number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]
print(number_grid[0][0])

# index of raw, index of column
# !!! remember all numbers of raws and columns start with 0 and NOT 1!!!!
print(number_grid[2][2])

print("\n")

for raw in number_grid:
    print(raw)

print("\n")

for raw in number_grid:
    for col in raw:
        print(col)
