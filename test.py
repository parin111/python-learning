shopping_list = [] #my shopping list

while len(shopping_list) < 2:
    
    fruit_input = input("fruit name")
    fruit_qty = input("how many fruits")
    shopping_list.append({fruit_input,fruit_qty})
print(shopping_list)
print(shopping_list[1])