# THE DYNAMIC TEXT AND NUMBER ANALLYZER

text = input("Enter sentence:  ")
step = int(input("Enter step:  "))

vowel_count = 0
consonant_count = 0
digit_sum = 0

for char in text:
    if char.isalpha():
        if char in "aeiouAEIOU":
            vowel_count = vowel_count + 1
        else:
            consonant_count = consonant_count + 1
    elif char.isdigit():
        digit_sum = digit_sum + int(char)

print("Vowel count: ", vowel_count)
print("Consonant count: ", consonant_count)
print("Sum of digits: ", digit_sum)