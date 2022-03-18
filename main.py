hairstyles = ["bouffant", "pixie", "dreadlocks",
              "crew", "bowl", "bob", "mohawk", "flattop"]
prices = [28, 27, 38, 18, 20, 34, 48, 38]
last_week = [3, 4, 3, 7, 4, 5, 4, 4]

total_price = 0

for i in prices:
    total_price += i

average_price = total_price/len(prices)

print("Average Haircut Price:", average_price)

new_prices = list(map(lambda x: x - 5, prices))

print("List of New Prices: ", new_prices)

total_revenue=0

for i in range(0, len(hairstyles)):
    total_revenue+=prices[i]*last_week[i]
    
print("Total Revenue: ", total_revenue)

average_daily_revenue = total_revenue/7

print("Average Daily Revenue: ", average_daily_revenue)

cuts_under_30=[]
cuts_under_30_prices=[]

for i in range(0,len(new_prices)):
    if new_prices[i]<30:
        cuts_under_30.append(hairstyles[i])
        cuts_under_30_prices.append(new_prices[i])

print("Cuts Under 30")
print("Haircut\t\tPrice")
print("===============================")
for i in range(0, len(cuts_under_30)):
    print("{:<10s}{:>4d}".format(cuts_under_30[i],cuts_under_30_prices[i]))
