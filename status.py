from PyInquirer import prompt

def show_status():
    # This function shows how much each user owes to the others
    # It also shows how much each user has to pay to the others
    f = open("expense_report.csv", "r")
    expenses = f.read().splitlines()
    f.close()
    f = open("users.csv", "r")
    users = f.read().splitlines()
    f.close()
    # Creating a dictionary of users
    users_dict = {}
    for user in users:
        users_dict[user] = {}
        for user2 in users:
            users_dict[user][user2] = 0
    # Calculating the amount each user owes to the others
    for expense in expenses:
        amount, label, spender, participants = expense.split(",")
        participants = participants.split("/")
        amount = int(amount)
        for participant in participants:
            if participant != spender:
                users_dict[spender][participant] += amount/len(participants)

    # Compute the results
    results = []
    for user in users_dict:
        for user2 in users_dict[user]:
            if users_dict[user][user2] != 0:
                results.append("{} owes {} to {}".format(user2, users_dict[user][user2], user) + '\n')
    # Print the results
    combined = ''.join(results)
    for user in users:
        # Verify if the user has no debt
        if str(user) + ' owes' not in combined:
            print("{} owes nothing".format(user))

    print(combined)

    return True