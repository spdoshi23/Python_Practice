N = int(input("Enter a number: "))
total_sum = 0
count = 0

for x in range(1, N+1):
    if x % 2 == 0:
        print(x)
        total_sum = total_sum + x
        count = count + 1
print(total_sum)
print(count)