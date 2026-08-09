# Write a program to calculate profit or loss.

cost_price = float(input('Enter cost price :'))
sell_price = float(input('Enter selling price :'))

if(cost_price < sell_price):
    profit = sell_price - cost_price
    print(f'Profit : {profit}')
elif(cost_price > sell_price):
    loss = cost_price - sell_price
    print(f'Loss : {loss}')
else:
    print('No Profit, No Loss')