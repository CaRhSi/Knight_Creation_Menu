import random


# Call for this when you want to create a new knight
def create_knight(knights):
    # Creates a new list for the Knight
    knights_data = []

    print("Lets create a knight!")

    # Set the information up for the knight
    knights_data.append(str(input("What is the knights name: ")))
    knights_data.append(str(input("What is the knights favourite drink: ")))

    # Ask for the knight's weapon choice
    while True:
        try:
            weapon_choice = input("Is the knight a sword or a mace user? (Enter 'sword' or 'mace'): ").lower()

            if weapon_choice == 'sword' or weapon_choice == 'mace':
                knights_data.append(weapon_choice)
                break
            else:
                raise ValueError

        except ValueError:
            print(f"{RED}Invalid input.{END} Please enter 'sword' or 'mace'.")

    # Ask for the knight's age
    while True:
        try:
            knight_age = int(input("How old is the knight?\nPlease enter a whole number: "))

            if 100 > knight_age > 15:
                knights_data.append(knight_age)
                break
            elif knight_age >= 100:
                raise ValueError("\nA bit old for a knight. The King has set the retirement age at 100\n")
            elif knight_age <= 15:
                raise ValueError("\nAre you insinuating that the King is using children in his army!?\n")
            else:
                raise ValueError("\nTry again\n")

        except ValueError as e:
            print(e)

    # Adds the information to the knight
    knights.append(knights_data)

# Call to change the order of the knights
def change_knight_order(knights):
    print("The order of the knights is currently: ")
    # Display the current knight order
    for i in range(len(knights)):
        count = i + 1
        print(str(count) + ". " + knights[i][0])

        # Print a new line for clarity after the last knight is printed
        if i == (len(knights) - 1):
            print("")

    while True:
        print("Please enter the order you wish the knights to be in.")
        print("Your entry must be in the form of numbers separated by spaces only.\n")

        # Get user input
        new_order = input("Enter the new order: ")
        print("")

        try:
            # Convert the input into a list of integers
            order_list = list(map(int, new_order.split()))

            # Check if the list contains exactly the same number of elements as the original knights list
            if len(order_list) != len(knights):
                raise ValueError("The number of entries does not match the number of knights.")

            # Check if the list contains valid positions
            if sorted(order_list) != list(range(1, len(knights) + 1)):
                raise ValueError("The order must contain each number from 1 to " + str(len(knights)) + " exactly once.")

            # Reorder the knights based on the new order
            reordered_knights = [knights[i - 1] for i in order_list]

            # Display the new order
            for i in range(len(reordered_knights)):
                count = i + 1
                print("The new order of the knights is " + str(count) + ". " + reordered_knights[i][0])

            # Update the original knights list with the reordered knights
            knights.clear()
            knights.extend(reordered_knights)
            return

        except ValueError as e:
            print(f"{RED}Invalid input:{END}", e)


# Call a knight and change their data
def change_data(knight):
    print("\n--- What would you like to update? ---")
    print("1: Knights name: " + knight[0])
    print("2: Knights favourite drink: " + knight[1])
    print("3: Knights favourite weapon: " + knight[2])
    print("4: Knights age: " + str(knight[3]))

    try:
        selection = int(input("\nSelect your option: "))

        if selection == 1:
            knight[0] = str(input("What is their new name: "))
            print("You knight's new name is: " + knight[0])
            return

        # Condition to handle the change of the favourite drink
        elif selection == 2:
            knight[1] = str(input("What is their new favourite drink: "))
            print("Your knight's new favourite drink is: " + knight[1])

        # Condition to handle change of weapon
        elif selection == 3:
            while True:
                try:
                    weapon_choice = input("What is the knights weapon of choice now? "
                                          "(Enter 'sword' or 'mace'): ").lower()

                    if weapon_choice == 'sword' or weapon_choice == 'mace':
                        knight[2] = weapon_choice
                        break
                    else:
                        raise ValueError

                except ValueError:
                    print(f"{RED}Invalid input.{END} Please enter 'sword' or 'mace'.")

            print("Your knight's weapon of choice is now: " + knight[2])

        # Condition to handle change of age
        elif selection == 4:
            while True:
                try:
                    new_age = int(input("What is the knights new age\nPlease enter a whole number: "))

                    if 100 > new_age > 15:
                        knights_data.append(knight_age)
                        break
                    elif new_age >= 100:
                        raise ValueError("\nA bit old for a knight. The King has set the retirement age at 100\n")
                    elif 0 < new_age <= 15:
                        raise ValueError("\nAre you insinuating that the King is using children in his army!?\n")
                    else:
                        raise ValueError("\nTry again\n")

                except ValueError as e:
                    print(e)

            print("Your knights age is now: " + knight[3])

        # Catch other input and loop back
        else:
            print(f"{RED}--- Please select a valid option ---{END}")

    except:
        print(f"{RED}--- Try Again! ---{END}")
        change_data(knight)


# Show the current knights and select one
def select_knight(knights):
    # Reset the list to print all the knights
    knight_index = 0
    print("What knight would you like to update?\n")
    while knight_index < int(len(knights)):
        print(str(knight_index + 1) + "- Knight's name:  " + str(knights[knight_index][0]))
        knight_index += 1

    selection = (int(input("\nSelect the knights number: ")) - 1)
    change_data(knights[selection])


# This is the menu and we make our selections
def menu(knights_number):
    # Print the display options
    print()
    print(" --- Main Menu --- ")
    print("What do you want to do?")
    print("1: Create a new Knight")
    print("2: Update your knight")
    print("3: The order of the knights")
    print("0: Exit")

    # Allows a selection to be tested
    try:

        # Takes the users selection option
        print()
        select = int(input("Selection number: "))
        print()  # Creates a blank line

        # Creates a new knight
        if select == 1:
            create_knight(knights)

            # Print out the Knight that was made
            print("\n--- Your Knight --- \n")
            print("Knight's name: " + str(knights[knights_number][0]))
            knights_number += 1
            menu(knights_number)

        elif select == 2:
            if int(len(knights)) == 0:
                print(f"{RED}Error:{END} You need to create a knight first!! \n")
            else:
                select_knight(knights)
            menu(knights_number)

        elif select == 3:
            # Can't change the order of the knight if there isn't at least two
            if int(len(knights)) <= 1:
                print(f"{RED}Error:{END} You need to create a more than one knight first!!")
            else:
                change_knight_order(knights)
            menu(knights_number)

        elif select == 0:
            print("--- All your Knights! --- \n")

            # Reset the knights_number, to count all the knights
            knights_number = 0

            while knights_number < int(len(knights)):
                print(str(knights_number + 1) + "- Knight's name:  " + str(knights[knights_number][0]))
                knights_number += 1

            if int(len(knights)) == 0:
                print("Wait... you have no knights! Have a number: " + str(random.randint(0, 100)))

        # Required for catching an integer
        else:
            print(f"{RED}--- Try Again! ---{END}")
            menu(knights_number)

    # We are looking for an integer selection
    except:
        print(f"{RED}--- Try Again! ---{END}")
        menu(knights_number)


# Setting the scene
RED = '\033[91m'
END = '\033[0m'
knights_number = 0
knights = []

# Run the program
menu(knights_number)
