from PyInquirer import prompt
user_questions = [
    {
        "type":"input",
        "name":"name",
        "message":"New User - Name: ",
    },
]

def add_user():
    # This function should create a new user, asking for its name
    infos = prompt(user_questions)
    # Writing the informations on external file
    f = open("users.csv", "a")
    f.write(f"{infos['name']}" + '\n')
    print("User Added !")
    return