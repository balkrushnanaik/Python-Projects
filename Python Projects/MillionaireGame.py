print("Welcome to Millionaire Game")
questions = [
    ["Who developed Python language?",
     "Dennis Ritchie", "James Gosling", "Guido van Rossum", "Bjarne Stroustrup",
     3],

    ["Which keyword is used to define a function in Python?",
     "function", "def", "fun", "define",
     2],

    ["Which symbol is used for comments in Python?",
     "//", "#", "/* */", "--",
     2],

    ["What is the correct file extension for Python files?",
     ".pt", ".pyt", ".py", ".python",
     3],

    ["Which data type is used to store text?",
     "int", "str", "bool", "list",
     2],

    ["What is output of 2 ** 3 ?",
     "5", "6", "8", "9",
     3],

    ["Which function is used to take input from user?",
     "get()", "input()", "scan()", "read()",
     2],

    ["Which data structure is unordered?",
     "list", "tuple", "set", "string",
     3],

    ["What is output of len([1,2,3]) ?",
     "2", "3", "4", "Error",
     2],

    ["Which keyword is used for loop in Python?",
     "loop", "iterate", "for", "repeat",
     3]
]

prizes = [10000,20000,30000,40000,50000,60000,70000,80000,90000,100000]

total_money = 0

for i in range(len(questions)):

    question = questions[i]

    print("\nQuestion", i+1)
    print(question[0])

    print(f"1. {question[1]}")
    print(f"2. {question[2]}")
    print(f"3. {question[3]}")
    print(f"4. {question[4]}")

    answer = int(input("Enter your answer (1-4): "))

    if answer == question[5]:
        total_money = prizes[i]
        print("Correct Answer")
        print("You won ₹", total_money)
    else:
        print("Wrong Answer")
        print("Correct answer was option", question[5])
        break

print("\nGame Over")
print("Total Prize Money Won = ₹", total_money)