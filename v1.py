# Vending machine with menu of drinks and snacks

# List of drinks and snacks with their corresponding codes and prices
items = {
    'A1': {'name': 'Coca-Cola', 'price': 1.50},
    'A2': {'name': 'Sprite', 'price': 1.50},
    'A3': {'name': 'Fanta', 'price': 1.50},
    'B1': {'name': 'Chips', 'price': 0.75},
    'B2': {'name': 'Peanuts', 'price': 0.50},
    'B3': {'name': 'Popcorn', 'price': 1.00}
}

# Function to display the menu of drinks and snacks
def display_menu():
    print('Welcome to the vending machine!')
    print('Here is a list of our drinks and snacks:')
    for code, item in items.items():
        print(code + ': ' + item['name'] + ' (' + str(item['price']) + ')')

# Function to get the user's selection and inputted money
def get_selection(total_money):
    # Get the user's selection
    selection = input('Enter the code for your selection (or enter Q to finish): ')
    # Check if the user wants to finish
    if selection == 'Q':
        # Give the user their money back
        print('Your total money is ' + str(total_money) + '.')
        return
    # Check if the selection is valid
    if selection in items:
        # Get the price of the selected item
        price = items[selection]['price']
        # Check if the user has enough money
        if total_money >= price:
            # Dispense the selected item
            print('Dispensing ' + items[selection]['name'] + '...')
            # Update the total money
            total_money -= price
            print('Your total money is ' + str(total_money) + '.')
            # Allow the user to make another selection
            get_selection(total_money)
        else:
            # Not enough money
            print('Not enough money. Please enter more money or select a different item.')
            # Allow the user to make another selection
            get_selection(total_money)
    else:
        # Invalid selection
        print('Invalid selection. Please try again.')
        # Allow the user to make another selection
        get_selection(total_money)

# Main function
def main():
    # Display the menu of drinks and snacks
    display_menu()
    # Get the user's inputted money
    money = float(input('Enter the amount of money: '))
    # Get the user's selection and inputted money
    get_selection(money)

# Run the main function
main()
