row = int(input("Enter the row value:"))
col = int(input("Enter the col value:"))

print("Square Pattern: row count = column count")
for i in range(0, row):
    for j in range(0, col):
        print("*", end=" ")
    print()

print("Half Pyramid(Right) Pattern: column_count = row_count+1 ")
for i in range(row):
    for j in range(i+1):
        print("*", end=" ")
    print()

print("Building a Floyds Triangle using Nested Loop: column_count = row_cout+1")
"""
1
2 3
4 5 6
7 8 9 10
"""
flag = 1
for i in range(row):
    for j in range(i+1):
        print(flag, end=" ")
        flag += 1
    print()