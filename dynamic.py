coins = [50, 25, 10, 5, 2, 1]

def find_min_coins(sum_:int):
    # індекс це сума
    min_coins_required = [0] + [float("inf")]*sum_     #мінімальна кількість монет
    last_coin_used = [0] * (sum_+1)  #остання монета суми
    
    
    for s in range(1, sum_ +1):
        for coin in coins:
            if s >= coin and min_coins_required[s-coin]+1 < min_coins_required[s]:
                min_coins_required[s] = min_coins_required[s-coin]+1
                last_coin_used[s] = coin
                
    
    count_coins = {}
    current_sum = sum_
    while current_sum > 0:
        coin = last_coin_used[current_sum]
        count_coins[coin] = count_coins.get(coin, 0)+1
        current_sum -=coin
        
    return count_coins
    
    
if __name__ =="__main__":
    result = find_min_coins(11)
    print(result)