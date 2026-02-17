num = int(input())
order = len(str(num))
temp = num
sum_val = 0

while temp > 0:
    digit = temp % 10
    sum_val += digit ** order
    temp //= 10

if sum_val == num:
    print("Armstrong")
else:
    print("Not Armstrong")