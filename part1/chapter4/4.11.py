pizzas = ["pa", "pb", "pc"]
print(pizzas)
for pizza in pizzas:
    print(pizza)

for pizza in pizzas:
    print(f"I like {pizza} pizza.")

print("I really love pizza!")

friend_pizzas = pizzas[:]
pizzas.append('pd')
friend_pizzas.append('pe')

print(pizzas)
print(friend_pizzas)