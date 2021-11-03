import csv

from PyInquirer import prompt

class User:
    def __init__(name,):
         self.name = name

user_questions = [
    {
        "type":"input",
        "name":"name",
        "message":"User - Name: ",
    },
]

def add_user():
    infos = prompt(user_questions)
    
    with open('users.csv', 'a', newline='') as csvfile:
        fieldnames = ['name']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(infos)     # Writing the informations on external file ¯\_(ツ)_/¯

    print("User Added !")
    return True