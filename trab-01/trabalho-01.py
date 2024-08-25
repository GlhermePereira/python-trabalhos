import random

def generate_random_list():
    return random.sample(range(0, 10), 5)

def prompt_number(number_list):
    while True:
        number = input("Enter a number or type 'Give up' to exit: ")

        if number.lower() == 'give up':
            print("You gave up. Goodbye!")
            break

        try:
            number = int(number)
        except ValueError:
            print("Please enter a valid number.")
            continue

        if number in number_list:
            print("Number found!")
            break
        else:
            print("Number not found. Try again.")


random_numbers = generate_random_list()
prompt_number(random_numbers)
