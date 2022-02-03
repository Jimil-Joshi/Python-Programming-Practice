arr = input("Enter row and column: ")
row,column = arr.split(",")
row = int(row)
column = int(column)
res = []
for x in range(row):
    rows= []
    for y in range(column):
        rows.append(x*y)
    res.append(rows)
print(res)
