def display_menu():
    print("\n------ MENU ------")
    print("[1] Ganja Brownie - ₱50")
    print("[2] Ganja Tea     - ₱30")
    print("[3] Ganja Cookie  - ₱40")
    print("[4] Checkout")
    print("[5] Cancel Order")


def main():
    print("Welcome to Ganja Life")
    print("-----------------------------------")

    print("[1] Menu")
    print("[2] Exit Application")
    
    title_choice = int(input("Enter your choice: "))

    if title_choice == 2:
        print("Thank you for visiting Ganja Life!")
        return

    cart = []
    total = 0

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
            print("\n--- Receipt ---")
            for item, price, qty in cart:
                subtotal = price * qty
                total += subtotal
                print(f"{item} x{qty} = ₱{subtotal}")
            print(f"TOTAL: ₱{total}")
            print("Thank you for your order!")
            break
        elif choice == 5:
            print("Order canceled.")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
