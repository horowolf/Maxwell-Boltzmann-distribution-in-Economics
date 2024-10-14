import random
import csv
from collections import Counter
import matplotlib.pyplot as plt

initial_amount = 1000
trade_unit = 100
trade_count_for_each = 100
population = 10000
balance = []
trade_count = []

def result():
    r = random.random() - 0.5
    if r < 0:
        return -1
    elif r > 0:
        return 1
    else:
        return result()
    
def trade(a: int, b: int):
    trade_count[a] = trade_count[a] + 1
    trade_count[b] = trade_count[b] + 1
    #if balance[a] < 1 or balance[b] < 1:
    #    return
    if result() > 0:
        if balance[b] > 0: # trade_unit * -10
            balance[a] = balance[a] + trade_unit
            balance[b] = balance[b] - trade_unit
    else:
        if balance[a] > 0: # trade_unit * -10
            balance[a] = balance[a] - trade_unit
            balance[b] = balance[b] + trade_unit

def picker(i: int):
    hit = int(random.random() * population)
    if hit == i:
        return picker(i)
    return hit

def trading():
    for count in range(trade_count_for_each):
        #for trader in range(population):
        #    if balance[trader] < trade_unit * 10:
        #        balance[trader] = balance[trader] + int(trade_unit * 0.2)
        for trader in range(population):
            hit = picker(trader)
            trade(trader, hit)

def init_state():
    for i in range(population):
        balance.append(initial_amount)
        trade_count.append(0)

def statistics():
    balance_distribution = Counter(balance)
    
    print("Balance statistics:")
    for bal, count in sorted(balance_distribution.items()):
        print(f"Balance: {bal}, count: {count}")
    
    plt.figure(figsize=(10, 6))
    
    balances = balance
    
    plt.hist(balances, bins=range(min(balances), max(balances) + trade_unit, trade_unit), edgecolor='black', alpha=0.7)
    
    plt.title('Balance Distribution')
    plt.xlabel('Balance')
    plt.ylabel('Number of Traders')
    
    plt.grid(axis='y', alpha=0.75)
    
    plt.tight_layout()
    plt.show()

def result_to_csv():
    with open('result.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Trader_ID', 'Balance', 'Trade_Count'])
        for trader_id in range(population):
            writer.writerow([trader_id + 1, balance[trader_id], trade_count[trader_id]])

init_state()
trading()
statistics()
result_to_csv()