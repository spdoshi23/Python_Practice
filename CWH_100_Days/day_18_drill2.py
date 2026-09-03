N = int(input("Enter a number: "))            #assume 34
digit_sum = 0

while (N>0):
    digit = N%10                              #(3.4)---remainder=4
    digit_sum = digit_sum + digit             #0+4=4
    N = N//10                                 #whole no. = 3           then, 3>0, 3%10---3,  7,   0

print(digit_sum)