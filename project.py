#1
pin = 1234
balance = 10000
attempts = 0
history = []

while attempts < 3:
    password = int(input("what's password?"))
    if password != pin:
        attempts += 1
        if attempts == 3:
            print("card blocked")
            break
        print("wrong password",3-attempts,"left")
        continue

    while True:
        print("""-------Menu-------
1. Balance
2. Deposit
3. Withdraw
4. Exit""")
        choice = int(input("enter menu no :"))
        if choice == 1:
            print("balance:",balance)

        elif choice == 2:
            dep = int(input("how much deposit ?"))
            if dep<0:
                print("amount must be above 0")
            else:
                balance += dep
                history.append(("deposit", dep))
                print("deposit amount",dep,"new balance",balance)

        elif choice == 3:
            withdraw =  int(input("how much withdrawl ?"))
            if withdraw <= 0:
                print("amount must be above 0")
            elif withdraw > balance:
                print("insufficient amount")
            else:
                balance-=withdraw
                history.append(("withdrawl",withdraw))
                print("withdrawl amount",withdraw,"new balance:",balance-withdraw)

        elif choice == 4:
            print("thank you for visiting , don't visit again")
            for items in history:
                print(items)
            break

        else:
            print("invalid input")
    break

# 2
students = {"Aman": [85, 90, 78], "Riya": [92, 88, 95], "Zoya": [70, 65, 80]}

for name,marks in students.items():
    avg = round(sum(marks)/len(marks),2)
    print(name,round(avg,2))

while True:
        print("""-------Menu-------
1. Add student
2. View all
3. Show topper
4. Exit""")
        
        choice = int(input("enter menu no:"))
        if choice == 1:
            name = input("add name :")
            if name in students:
                print("students already exist")
            else:
                marks = []
                while len(marks)<3:
                    m = int(input("put number"))
                    if 0<= m<= 100:
                        marks.append(m)
                    else:
                        print("invalid mark, try again")
                students[name]=marks
                print("added name",name)

        if choice == 2:
            for name, marks in students.items():
                avg = round(sum(marks)/len(marks),2)
                if avg > 85:
                    grade = "A"
                elif avg> 70:
                    grade = "B"
                elif avg>50:
                    grade = "C"
                else:
                    grade = "f"
                print(name,avg,grade)

        if choice == 3:
            highest=0
            topper = ""
            for name,marks in students.items():
                avg = round(sum(marks)/len(marks),2)
                if avg>highest:
                    highest=avg
                    topper = name

            print("Topper:",topper)

        elif choice == 4:
            print("Goodbye")
            break
        else:
            print("invalid output")
