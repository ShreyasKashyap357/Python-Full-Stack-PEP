def user_profile():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    hobbies = input("Enter your hobbies (comma separated): ")
    hobbies_list = [hobby.strip() for hobby in hobbies.split(',')]
    user_data = {'name': name, 'age': age, 'hobbies': hobbies_list}
    return user_data

def expense_tracker():
    num = int(input("Enter the number of expenses you want to track: "))
    expense = 0
    categories = set()
    for i in range(num):
        categories.add(input(f"Enter the category of the {i+1}th expense: "))
        while True:
            try:
                expense += float(input(f"Enter the amount for the {i+1}th expense: "))
                break
            except ValueError:
                print("Invalid input! Please enter a numeric value for the expense amount.")
    print(f"Total expenses: {expense:.2f}")
    print(f"Unique categories of expenses: {', '.join(categories)}")

def contact_book():
    contacts = {}
    while len(contacts) < 3:  # Ensure at least 3 contacts are added
        print("\nPlease add 3 contacts (name & age required).")
        name = input("Enter contact name: ")
        age = input("Enter age: ")
        if age.isdigit():
            age = int(age)
        else:
            print("Invalid age. Please enter a numeric value.")
            continue
        contacts[name] = {'age': age}
        print(f"Contact '{name}' added successfully.")
    while True:
        print("\nContact Book Menu:")
        print("1. View Contacts")
        print("2. Compute Average Age")
        print("3. Show Contacts Over Age 25")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            for name, details in contacts.items():
                print(f"Name: {name}, Age: {details['age']}")
        elif choice == '2':
            avg_age = sum(contact['age'] for contact in contacts.values()) / len(contacts)
            print(f"Average age of contacts: {avg_age:.2f}")
        elif choice == '3':
            over_25 = [name for name, details in contacts.items() if details['age'] > 25]
            print("Contacts over age 25:", ', '.join(over_25) if over_25 else "No contacts are older than 25.")
        elif choice == '4':
            print("Exiting the contact book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def string_fun():
    user_sentence = input("How was your day? Please describe it in a sentence: ")
    # Convert to uppercase
    print(user_sentence.upper())
    # Count vowels using a list comprehension
    vowels = sum(1 for char in user_sentence if char.lower() in 'aeiou')
    print(f"Number of vowels in your sentence: {vowels}")
    # Separate words and punctuation using a list comprehension
    words = [word[:-1] if not word[-1].isalnum() else word for word in user_sentence.split()] + \
            [word[-1] for word in user_sentence.split() if not word[-1].isalnum()]
    # Reverse word order while preserving punctuation placement
    reversed_sentence = [words[i] for i in range(len(words) - 1, -1, -1)]
    # Attach punctuation properly
    last_punctuation = reversed_sentence.pop() if reversed_sentence[-1] in ",.!?" else ""
    reversed_sentence[-1] += last_punctuation if last_punctuation else ""
    print("Reversed sentence with alphanumeric words:", ' '.join(reversed_sentence))

def comprehensions():
    print("Generating data using list and dictionary comprehensions!")
    # List comprehension for squares
    squares = [x**2 for x in range(1, 11)]
    print("List of squares:", squares)
    # Dictionary comprehension for cubes
    cube_dict = {i: i**3 for i in range(1, 6)}
    print("Dictionary of cubes:", cube_dict)

while True:
    try:
        choice = int(input("\nWelcome to your personal dashboard! Please choose an option:\n"
                           "1. User Profile\n"
                           "2. Expense Tracker\n"
                           "3. Contact Book\n"
                           "4. String Fun\n"
                           "5. Comprehensions\n"
                           "6. Exit\n"
                           "Enter your choice (1-6): "))
        if 1 <= choice <= 6:  # Ensure choice is within valid range
            if choice == 6:
                print("Exiting the dashboard. Goodbye!")
                break  # Exit the loop only when choice is 6
            # Execute selected option
            elif choice == 1:
                user_profile()
            elif choice == 2:
                expense_tracker()
            elif choice == 3:
                contact_book()
            elif choice == 4:
                string_fun()
            elif choice == 5:
                comprehensions()
        else:
            print("Invalid choice! Please enter a number between 1 and 6.")
    except ValueError:
        print("Invalid input! Please enter a numeric value between 1 and 6.")
    except KeyboardInterrupt:
        print("\nExiting dashboard. Goodbye!")
        exit()  # Handle Ctrl+C gracefully
