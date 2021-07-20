# Liste 0 bis 9
my_list = []
for i in range(10):
    my_list.append(i)

# List Comprehension
#           val - iterable
my_list2 = [i for i in range(10)]
# Quadrat
my_list3 = [i**2 for i in range(10)]

# Multi-dim List
# Matrix (3 rows, 2 columns)
M = [[1, 2],
     [3, 4],
     [5, 6]]

NUM_ROWS = 2
NUM_COLS = 3
M2 = [[i + j for j in range(NUM_COLS)] for i in range(NUM_ROWS)]
print(M2)
