import time

# Набір монет (можна змінювати)
coins = [50, 25, 10, 5, 2, 1]

# ----- Greedy Algorithm -----
def find_coins_greedy(amount):
    result = {}
    for coin in sorted(coins, reverse=True):
        count = amount // coin
        if count > 0:
            result[coin] = count
            amount -= coin * count
    return result

# ----- Dynamic Programming -----
def find_min_coins(amount):
    # Ініціалізація
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    last_coin = [-1] * (amount + 1)
    
    # Динаміка
    for coin in coins:
        for i in range(coin, amount + 1):
            if dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                last_coin[i] = coin

    # Відновлення розв’язку
    result = {}
    i = amount
    while i > 0 and last_coin[i] != -1:
        c = last_coin[i]
        result[c] = result.get(c, 0) + 1
        i -= c
    
    return result

# ----- Порівняння продуктивності -----
def compare_algorithms(amount):
    print(f"\n=== Test amount: {amount} ===")
    
    # Greedy
    start = time.time()
    greedy_result = find_coins_greedy(amount)
    greedy_time = time.time() - start
    print(f"Greedy result: {greedy_result}, time: {greedy_time:.6f} sec")
    
    # DP
    start = time.time()
    dp_result = find_min_coins(amount)
    dp_time = time.time() - start
    print(f"DP result: {dp_result}, time: {dp_time:.6f} sec")
    
    return greedy_time, dp_time

# ----- Приклад використання -----
if __name__ == "__main__":
    # Тестова сума
    test_amounts = [113, 275, 999, 1234, 5000]
    
    for amount in test_amounts:
        compare_algorithms(amount)