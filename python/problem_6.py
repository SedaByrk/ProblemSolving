sum1 = 0
sum2 = 0

for i in range(1, 101):
    sum1 += i*i

for j in range(1, 101):
    sum2 += j
sum2 = sum2 * sum2
diff = sum2 - sum1
print(diff)
