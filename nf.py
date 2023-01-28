product = [
    {'Product': 'Egg', 'Value': 10},
    {'Product': 'Meat', 'Value': 20},
    {'Product': 'Onion', 'Value': 15}
    ]

# adjustPrice = [x['Value']*1.20 for x in product]

# print(adjustPrice)

# adjustUsingLambda = map(lambda x: x['Value']*1.20, product)
# print(list(adjustUsingLambda))

filteredProduct = filter(lambda x: x['Product'] == 'Egg', product)
print(list(filteredProduct))