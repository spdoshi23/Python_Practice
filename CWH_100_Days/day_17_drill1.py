N = int(input("Enter an integer N: "))

total_sum = 0

for x in range(1, N+1):
    if x % 3 ==0:
        print(x)
        total_sum = total_sum + x
print(total_sum)