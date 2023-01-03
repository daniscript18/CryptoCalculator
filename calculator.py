def is_float(value):
    try:
        float(value)
    except ValueError:
        print("The value you entered is invalid")
        exit()

def is_str(value):
    try:
        str(value)
    except ValueError:
        print("The value you entered is invalid")
        exit()

difficulty = input("Difficulty per block = ") or "none"; is_float(difficulty); difficulty = float(difficulty);
hashrate = input("Miner hashrate = ") or "none"; is_float(hashrate); hashrate = float(hashrate)
reward = input("Block reward = ") or "none"; is_float(reward); reward = float(reward)
price = input("Coin price = ") or "none"; is_float(price); price = float(price)

cripto = input("Crypto prefix (bitcoin) = ") or "bitcoin"; is_str(cripto); cripto = str(cripto)
currency = input("Currency prefix (dollars) = ") or "dollars"; is_str(currency); currency = str(currency)

block_time = (difficulty / hashrate)
coin_hour = ((3600 / block_time) * reward)
coin_day = (coin_hour * 24)
earnings_hour = (coin_hour * price)
earnings_day = (coin_day * price)

print(f"» Earnings per hour in {cripto}: {coin_hour}")
print(f"» Earnings per day in {cripto}: {coin_day}")
print(f"» Earnings per hour in {currency}: {earnings_hour}")
print(f"» Earnings per day in {currency}: {earnings_day}")