Skip to main content
Google Classroom
Classroom
BTech-SE-5C-2025
5C
Home
Calendar
Gemini
Enrolled
To-do
D
DBMS-VA
C
D
DBMS-LAB
F & C
B
BTech-SE-5C-2025
5C
U
UE23CS252B-1: CN
C
Archived classes
Settings
Material details
Labs
RADHIKA M HIRANNAIAH PESU RR CSE STAFF
•
Aug 20 (Edited Yesterday)

Lab_1_RequirementEngineering_student_handout.pdf
PDF

Lab 1 - Requirements/UML
Google Forms

Lab_2_Jira_Student_Handout.pdf
PDF

Lab 2 - Jira
Google Forms

Lab_3_Architecture_Student_handout.pdf
PDF

Lab 3: Component Modelling and Architecture Pattern
Google Forms

Lab_4_VibeCoding_Handout.pdf
PDF

Lab 4 - Vibe Coding
Google Forms

Lab_5_Static_code_analysis_Student_handout.pdf
PDF

inventory_system.py
Text

Lab 5: Static Code Analysis
Google Forms
Class comments

Add class comment…

import json
import logging
from datetime import datetime

# Global variable
stock_data = {}

def addItem(item="default", qty=0, logs=[]):
    if not item:
        return
    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append("%s: Added %d of %s" % (str(datetime.now()), qty, item))

def removeItem(item, qty):
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except:
        pass

def getQty(item):
    return stock_data[item]

def loadData(file="inventory.json"):
    f = open(file, "r")
    global stock_data
    stock_data = json.loads(f.read())
    f.close()

def saveData(file="inventory.json"):
    f = open(file, "w")
    f.write(json.dumps(stock_data))
    f.close()

def printData():
    print("Items Report")
    for i in stock_data:
        print(i, "->", stock_data[i])

def checkLowItems(threshold=5):
    result = []
    for i in stock_data:
        if stock_data[i] < threshold:
            result.append(i)
    return result

def main():
    addItem("apple", 10)
    addItem("banana", -2)
    addItem(123, "ten")  # invalid types, no check
    removeItem("apple", 3)
    removeItem("orange", 1)
    print("Apple stock:", getQty("apple"))
    print("Low items:", checkLowItems())
    saveData()
    loadData()
    printData()
    eval("print('eval used')")  # dangerous

main()
inventory_system.py
Displaying inventory_system.py.