import random
import json

# Data file paths
users_data_file = 'users_data.json'
agents_data_file = 'agents_data.json'

# Function to read data from file
def read_data(data_file):
    try:
        with open(data_file, 'r') as file:
            return [json.loads(line) for line in file]
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    # Function to write data to file
def write_data(data, data_file):
    with open(data_file, 'a') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
        # json.dump(data, file, ensure_ascii=False)
        file.write('\n')  # Add a new line after writing data

# Function to generate a new account number
def generate_account_number():
    return random.randint(1000000000, 9999999999)

# Function to create a new account for users
def create_user_account():
    global users_data

    new_user = {}
    for detail in newusers_one:
        new_user[detail] = input(f"Enter {detail}: ")

    new_user['account_num'] = generate_account_number()
    new_user['balance'] = 0

    users_data.append(new_user)
    write_data(new_user, users_data_file)

    print("Your account has successfully been created")

# Function to create a new account for agents
def create_agent_account():
    global agents_data

    new_agent_id = generate_account_number()
    new_agent_pin = input("Enter agent's PIN: ")

    new_agent = {
        'agent_id': new_agent_id,
        'pin': new_agent_pin
    }

    agents_data.append(new_agent)
    write_data(new_agent, agents_data_file)

    print("Agent account has successfully been created")

# Function to display account information
def display_account_info():
    global users_data

    my_acct = int(input("Please input your account number: "))
    my_pin = input("Please input your pin: ")

    for user_info in users_data:
        if user_info['account_num'] == my_acct and user_info['pin'] == my_pin:
            print(f"Account Name: {user_info['FirstName']} {user_info['LastName']}\nBalance: ${user_info['balance']}\nAccount Number: {user_info['account_num']}")
            return
    print("Invalid account number or pin.")
    #function to deposit money to users account
def agent_deposit():
    global users_data, agents_data

    agent_id = int(input("Please input agent ID: "))
    agent_pin = input("Please input agent PIN: ")

    agent_valid = False
    for agent in agents_data:
        if agent['agent_id'] == agent_id and agent['pin'] == agent_pin:
            agent_valid = True
            break
    if agent_valid:
        my_acct = int(input("Please input the user's account number: "))
        amount = float(input("Input amount to be deposited: "))

        for user_info in users_data:
            if user_info['account_num'] == my_acct:
                user_info['balance'] += amount
                write_data(user_info, users_data_file)
                print(f"The sum of ${amount} has been deposited to {user_info['FirstName']} {user_info['LastName']}")
                return
        print("User account not found.")
    else:
        print("Invalid agent ID or PIN.")
# Function for user-to-user transfer
def transfer_funds():
    global users_data

    sender_acct_num = int(input("Input sender's account number: "))
    receiver_acct_num = int(input("Input receiver's account number: "))
    sender_pin = input("Input sender's account pin: ")
    amount = float(input("Input amount to transfer: "))

    sender_found = False
    receiver_found = False

    for user_info in users_data:
        if user_info['account_num'] == sender_acct_num and user_info['pin'] == sender_pin:
            sender_found = True
            if user_info['balance'] >= amount:
                user_info['balance'] -= amount
                for recipient_info in users_data:
                    if recipient_info['account_num'] == receiver_acct_num:
                        receiver_found = True
                        recipient_info['balance'] += amount
                        print(f"${amount} has successfully been transferred to {recipient_info['FirstName']} {recipient_info['LastName']}")
                        break

    if not sender_found:
        print("Invalid sender account number or pin.")
    elif not receiver_found:
        print("Invalid receiver account number.")
    else:
        # Update the data file after successful transfer
        with open(users_data_file, 'w') as file:
            for user_info in users_data:
                json.dump(user_info, file, ensure_ascii=False)
                file.write('\n')
#Function to change user PIN
def change_pin():
    global users_data

    my_acct = int(input("Please input your account number: "))
    my_first_name = input("Please enter the first three letters of your first name: ")

    for user_info in users_data:
        if user_info['account_num'] == my_acct and user_info['FirstName'][:3] == my_first_name[:3]:
            new_pin = input("Enter new PIN: ")
            user_info['pin'] = new_pin
            write_data(user_info, users_data_file)
            print("PIN successfully changed.")
            return

    print("Invalid account number or first name.")

# ... (other functions)

# Main program loop
print("Welcome to Jericco's Mobile Bank!")
users_data = read_data(users_data_file)
agents_data = read_data(agents_data_file)

newusers_one = ["FirstName", "LastName", "Age", "pin"]

while True:
    menu = int(input("1. Create User Account\n2. Create Agent Account\n3. Display Account Info\n4. Agent Deposit\n5. Transfer Funds\n6. Change Pin\n7. Exit App\nPlease choose from the Menu: "))

    if menu == 1:
        acct = int(input("Input 1 to start\nPlease proceed with your account creation: "))
        if acct == 1:
            create_user_account()
    elif menu == 2:
        create_agent_account()
    elif menu == 3:
        display_account_info()
    elif menu == 4:
        agent_deposit()
    elif menu == 5:
        transfer_funds()
    elif menu == 6:
        change_pin()
    elif menu == 7:
        print("Thank you for using Jericco's Mobile Bank!")
        break
    else:
        print("Invalid option. Please try again.")
