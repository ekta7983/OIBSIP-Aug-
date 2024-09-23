import os
import getpass

# File to store user credentials
USER_DATA_FILE = "users.txt"

# Function to register a new user
def register():
    print("=== Register ===")
    username = input("Enter a username: ")
    password = getpass.getpass("Enter a password: ")

    # Check if user already exists
    if user_exists(username):
        print("User already exists. Please choose a different username.")
        return

    # Save the user credentials
    with open(USER_DATA_FILE, "a") as f:
        f.write(f"{username},{password}\n")
    
    print(f"User {username} registered successfully!")

# Function to check if a user exists
def user_exists(username):
    if not os.path.exists(USER_DATA_FILE):
        return False
    
    with open(USER_DATA_FILE, "r") as f:
        for line in f:
            stored_username, _ = line.strip().split(",")
            if stored_username == username:
                return True
    return False

# Function to validate user credentials
def login():
    print("=== Login ===")
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")

    # Check credentials
    if validate_credentials(username, password):
        print("Login successful!")
        secured_page(username)
    else:
        print("Invalid username or password.")

# Function to validate credentials
def validate_credentials(username, password):
    if not os.path.exists(USER_DATA_FILE):
        return False

    with open(USER_DATA_FILE, "r") as f:
        for line in f:
            stored_username, stored_password = line.strip().split(",")
            if stored_username == username and stored_password == password:
                return True
    return False

# Secured page after successful login
def secured_page(username):
    print(f"Welcome, {username}!")
    print("This is a secured page, only accessible after login.")
    # You can add more functionality here

# Main program flow
def main():
    while True:
        print("\n=== Menu ===")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
