arr = list(map(int, input().split()))
n = len(arr) + 1

expected = n * (n + 1) // 2
actual = sum(arr)

print(expected - actual)

# output :  