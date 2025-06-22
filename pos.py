def display_menu():
    print("\n------ MENU ------")
    print("[1] Ganja Brownie - ₱50")
    print("[2] Ganja Tea     - ₱30")
    print("[3] Ganja Cookie  - ₱40")
    print("[4] Checkout")
    print("[5] Cancel Order")


def print_receipt(cart):
    total = 0
    print("\n--- Receipt ---")
    for item, price, qty in cart:
        subtotal = price * qty
        total += subtotal
        print(f"{item} x{qty} = ₱{subtotal}")
    print(f"TOTAL: ₱{total}")
    print("Thank you for your order!")


def new_transaction():
    while True:
        cart = []

        while True:
            display_menu()
            choice = int(input("Select item number: "))

            if choice == 1:
                qty = int(input("Enter quantity: "))
                cart.append(("Ganja Brownie", 50, qty))
            elif choice == 2:
                qty = int(input("Enter quantity: "))
                cart.append(("Ganja Tea", 30, qty))
            elif choice == 3:
                qty = int(input("Enter quantity: "))
                cart.append(("Ganja Cookie", 40, qty))
            elif choice == 4:
                print_receipt(cart)
                break
            elif choice == 5:
                print("Order canceled.")
                break
            else:
                print("Invalid choice. Try again.")

        # Ask for new transaction or exit
        again = input("\nWould you like to start a new transaction? (y/n): ").lower()
        if again != 'y':
            print("Thank you for visiting Ganja Life!")
            break


def main():
    print("Welcome to Ganja Life")
    print("-----------------------------------")
    print("[1] Menu")
    print("[2] Exit Application")

    title_choice = int(input("Enter your choice: "))

    if title_choice == 1:
        new_transaction()
    else:
        print("Thank you for visiting Ganja Life!")


if __name__ == "__main__":
    main()
