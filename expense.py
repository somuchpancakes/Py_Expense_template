import os
import csv

from PyInquirer import prompt

class Expense:
     def __init__(amount, label, spender):
         self.amount = amount
         self.label = label
         self.spender = spender

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
        "message":"Who is the spender ?",
        "choices": []
    },
]

def get_users():
    with open('users.csv', newline='') as csvfile:
        users_list_csv = csv.reader(csvfile, delimiter=',')
        for row in users_list_csv :
            expense_questions[2]["choices"].append("".join(row))

def new_expense(*args):

    if (os. stat("users.csv").st_size == 0):
        print("You must define at least one user !")
        return False

    get_users() #Load the users.csv

    infos = prompt(expense_questions)
    
    with open('expense_report.csv', 'a', newline='') as csvfile:
        fieldnames = ['amount', 'label', 'spender']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(infos) # Writing the informations on external file ¯\_(ツ)_/¯

    print("Expense Added !")
    return True