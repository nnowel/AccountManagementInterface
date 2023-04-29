def compliment():

    name = input('Enter your name:') # You can ask for additional input within a function.
    print(f'{name} is most likely a decent person.')



def random_number():

    import random

    print(f'Your random number is {random.randint(1,10)}.')



def interface():

    choice = ''
    while choice != '9':

        # Print the interface options
        print("1: Get a half-hearted compliment.")
        print("2: Get a random number.")
        print("9: Exit.")

        # Collect user input
        choice = input('Select an option:')

        if choice == '1':
            compliment()
        elif choice == '2':
            random_number()
        elif choice == '9':
            print("Shutting down...")
        else:
            print("Please select an actual option.")

interface()