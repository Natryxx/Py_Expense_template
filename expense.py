from PyInquirer import prompt

def getUsers():
    list = []
    f = open("users.csv", "r")
    users = f.read().splitlines()
    for user in users:
        list.append({"name": user.strip()})
    return list

expense_questions = [
    {
        "type":"input",
        "name":"amount",
        "message":"New Expense - Amount: ",
    },
    {
        "type":"input",
        "name":"label",
        "message":"New Expense - Label: ",
    },
    {
        "type":"list",
        "name":"spender",
        "message":"New Expense - Spender: ",
        # Get the list of users without \n from the file users.csv
        "choices": getUsers()
    },
    {
        "type":"checkbox",
        "name":"participants",
        "message":"New Expense - Participants: ",
        # Get a json list of users name from the file users.csv
        "choices": getUsers(),
    },
]

def new_expense(*args):
    infos = prompt(expense_questions)
    #Check if spender is not in participants
    if infos['spender'] not in infos['participants']:
        infos['participants'].append(infos['spender'])
    # Writing the informations on external file might be a good idea ¯\_(ツ)_/¯
    f = open("expense_report.csv", "a")
    # Write the expense in the file expense_report.csv with the following format: amount,label,spender,participant&participant&participant
    f.write("{},{},{},{}".format(infos['amount'],infos['label'],infos['spender'],"/".join(infos['participants'])) + '\n')
    print("Expense Added !")
    return True
