# Shopping cart program

# creates empty lists to store foods, quantities and their prices, and a variable "total"
foods = []
prices =[]
quantities = []
total = 0

# Loop to let the user add items to the cart
while True:
    food = input("Enter a food to buy (q to quit): ")
    if food.lower() == "q": # Lets the user input "q" in any case to exit the loop
        break
    else:
        # ask for the price of the food and add both to their lists
        food = food.capitalize() # Capitalise the first letter
        price = float(input(f"Enter the price of a {food}: €"))
        quantity = int(input(f"How much of this are you buying? "))
        foods.append(food)
        prices.append(price * quantity)
        quantities.append(quantity)

# prints the cart header
print("----- YOUR CART -----")

# Alternative that prints all the foods in the cart on a single line
# for food in foods:
#     print(food, end=" ")

# prints all the foods in the cart, each on a new line with their position, quantity and price
for i, (food, price) in enumerate(zip(foods, prices), start=1):
    print(f"{i}. {food} (x{quantity}) - €{price:.2f}")

# adds up all the prices to get the total
for price in prices:
    total += price
    
print("------ SUMMARY  ------")
# print the total price
print(f"Your total is: €{total:.2f}")