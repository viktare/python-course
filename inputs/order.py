
not_available = ['tomato', 'tuna']

sandwich_orders = []
delivered_sandwiches = []

ordering = True
while ordering:
    sandwich = input('Tell me the sandwich ')
    if(sandwich == 'quit'):
        ordering = False
    else:
        sandwich_orders.append(sandwich)

for ing in not_available:
    if ing in sandwich_orders:
        sandwich_orders.remove(ing)
        another = input(f"I'm sorry, the {ing} is not available, would you like to order something else? ")
        if another == 'no':
            continue
        new_sandwich = input(f"Which ingredient? ")
        
        sandwich_orders.append(new_sandwich)

while sandwich_orders:
    current = sandwich_orders.pop()
    print(f"You're {current} sandwich is ready!")
    delivered_sandwiches.append(current)

print(sandwich_orders)
print(delivered_sandwiches)