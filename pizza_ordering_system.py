# Display price menu once at the start
print("===== PIZZA PRICE MENU =====")
print("Small Pizza  : 100 Rs")
print("Medium Pizza : 200 Rs")
print("Large Pizza  : 300 Rs")
print("Pepperoni    : 30 Rs (Small) / 50 Rs (Medium/Large)")
print("Extra Cheese : 20 Rs")
print("=============================")

total_bill = 0
pizza_count = 0

while True:
    pizza_count += 1
    print(f"\n--- Pizza #{pizza_count} ---")
    
    # Get size
    size = input("What size pizza you want (S/M/L)? ").strip().upper()
    while size not in ['S', 'M', 'L']:
        size = input("Invalid input. Please enter S, M, or L: ").strip().upper()
    
    # Calculate base price
    if size == 'S':
        bill = 100
        print("Small Pizza Price is 100 Rs")
    elif size == 'M':
        bill = 200
        print("Medium Pizza Price is 200 Rs")
    else:  # size == 'L'
        bill = 300
        print("Large Pizza Price is 300 Rs")
    
    # Pepperoni
    add_pepperoni = input("Do you want Pepperoni (Y/N)? ").strip().upper()
    if add_pepperoni == 'Y':
        if size == 'S':
            bill += 30
            print("Added Pepperoni for 30 Rs")
        else:
            bill += 50
            print("Added Pepperoni for 50 Rs")
    
    # Extra cheese
    extra_cheese = input("Do you want extra cheese (Y/N)? ").strip().upper()
    if extra_cheese == 'Y':
        bill += 20
        print("Added extra cheese for 20 Rs")
    
    print(f"Price for this pizza: {bill} Rs")
    total_bill += bill
    
    # Ask if user wants another pizza
    another = input("\nDo you want to order another pizza? (Y/N): ").strip().upper()
    if another != 'Y':
        break

print(f"\n===== FINAL BILL =====")
print(f"Total pizzas ordered: {pizza_count}")
print(f"Your total bill is: {total_bill} Rs")
print("=====================")
