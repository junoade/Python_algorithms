M = int(input())
coins = [500,100,50,10]
coin_result = []
min_result = 0

for idx in range(0,len(coins)):   
    amount = M//coins[idx]
    coin_result.append(amount)
    M=M%coins[idx]

total = 0
for num in coin_result:
    print(num, end=" ")
    total += num
print()
print(total)


print(f"{total} 냥냥 ")
print("{} 냥냥".format(total))
