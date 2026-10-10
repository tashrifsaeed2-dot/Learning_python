

start_for = 1
end_for = 10
answer = 1
for i in range(start_for, end_for+1, 1):
    answer *= 2
    print(f"2 got multiplied for {i} times , so the answer aftyer {i} iteration = {answer}")

print()
print("s"*27)
print()


start_while = 1
end_while = 10
i = start_while
answer = 1
while (i <= end_while):
    answer *= 2
    print(f"2 got multiplied for {i} times , so the answer aftyer {i} iteration = {answer}")
    i += 1