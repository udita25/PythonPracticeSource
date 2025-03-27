n = int(input("Enter a number: "))

#approach 1
sum = 0
for i in range(1, n+1):
    sum += i

print(sum)

#approach 2
sum1 = n * (n + 1) // 2
print(sum1)