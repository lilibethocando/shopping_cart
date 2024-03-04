from datetime import datetime

cart = {}

def buy(item, price, quantity):
    if item not in cart:
        cart[item] = {'price':price, 'quantity':quantity}
    else:
        cart[item]['quantity'] += quantity
    return cart 

def remove(item):
    if item in cart:
        del cart[item]
        print(f"The item: {item} has been removed and your shopping cart has been updated")
    else:
        print(f"{item} is not in the shopping cart, validate the name of the item and try it again!")

def show_cart():
    total_price_all = 0
    if not cart:
        print("Your cart is empty!")
    for key, value in cart.items():
        total_price_all += value['price']*value['quantity']
        print("." * 80)
        print(f"Product: {key.capitalize()} | Unit Price = ${value['price']:.2f} | Quantity = {value['quantity']} | Total price = ${value['price']*value['quantity']:.2f}")
        print("." * 80)
    print(f"The total amount of your shopping cart is ${total_price_all:.2f}")

def print_receipt():
    date = datetime.now()
    print("\t\t\t\tLILLY'S STORE")
    print("="*80)
    print(f"Thank you for shopping at Lilly's store on {date.strftime('%m/%d/%Y')}, {date.strftime('%I:%M %p')}")
    print("Find the details of your purchase below")
    shopping = show_cart()
    print("*You have up to 30 days for any returns and refunds*")



def main():
    print("-"*100)
    print("Welcome to Lilly's store, we hope you find what you are looking for!")
    print("-"*100)
    while True:
        menu = input("Select one of the following options: Buy, Remove, Show Cart, Print or Exit:\n").lower()
        if menu == 'buy':
            item = input("Type name of the item:\n").lower()
            price = float(input("Enter the price:\n$"))
            quantity = int(input("How many items?\n"))
            cart = buy(item, price, quantity)
        elif menu == 'remove':
            item = input("Type name of the item:\n").lower()
            remove_item = remove(item)
        elif menu == 'show cart':
            show = show_cart()
        elif menu == 'print':
            receipt = print_receipt()
        elif menu == 'exit':
            receipt = print_receipt()
            print("Thank you for shopping with us!")
            print("="*80)
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()