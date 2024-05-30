pizza = {
    'crust': 'thick',
    'toppings': ['mu', 'extra'],
}

print(pizza['crust'])
print(pizza['toppings'])

for topping in pizza['toppings']:
    print(f"\t{topping}")