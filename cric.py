import random
import mysql.connector

print("""
Welcome To Cricket Game
_______________________
""")


mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='7321755631'
)
mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS cricket_db")
mycursor.execute("USE cricket_db")

mycursor.execute("""
    CREATE TABLE IF NOT EXISTS cricket(
        sno INT NOT NULL,
        date DATE NOT NULL,
        name VARCHAR(25) NOT NULL,
        run INT NOT NULL,
        status VARCHAR(10) NOT NULL
    )
""")
mycursor.execute("""
    CREATE TABLE IF NOT EXISTS login(
        username VARCHAR(25) NOT NULL,
        password VARCHAR(25) NOT NULL
    )
""")
mycursor.execute("""
    CREATE TABLE IF NOT EXISTS sno(
        id INT NOT NULL
    )
""")

mydb.commit()

mycursor.execute("select * from sno")
r = 0
for i in mycursor:
    r = 1
if r==0:
    mycursor.execute("insert into sno values(0)")
    mydb.commit()

mycursor.execute("select * from login")
r = 0
for i in mycursor:
    r = 1
if r==0:
    mycursor.execute("insert into login values('admin', 'ng')")
    mydb.commit()


while True:
    print("""
1. Login
2. Instructions
3. Data
4. Exit
""")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        password = input("Enter your password: ")
        mycursor.execute("select * from login")
        for i in mycursor:
            t_user, t_password = i
            if( password == t_password):
                Name = input("Enter your name: ")

                #Cricket game
                print("\n----------start game--------")

                #Toss
                print("\nHere comes the Toss")
                toss = input("Choose heads or tails: ").lower()

                random_toss = random.randint(1,2)    # 1 for heads, 2 for tails
                random_opt = random.randint(1,2)     # 1 for bat, 2 for ball

                u_opt = 0
                c_opt = 0

                if random_toss==1 and toss == "heads":
                     print("\nYou won the toss")

                     u_opt= (input("Choose bat or ball: ")).lower()

                elif random_toss == 2 and toss == "tails":
                    print("\nYou won the toss")

                    u_opt= (input("Choose bat or ball: ")).lower()

                else:
                    print("\nYou lost the toss")

                    if random_opt == 1:
                        c_opt = "bat"
                        print("Computer choose to", c_opt)

                    elif random_opt == 2:
                        c_opt = "ball"
                        print("Computer choose to", c_opt)

                # First Innings
                print("\n---- First Innings Begins ------")

                runs_1 = 0

                wickets_1 = 0

                balls_1 = 0

                while wickets_1 != 2 and balls_1 != 12:
                    u_choice = int(input("\nChoose any number from 1 to 6: "))

                    c_choice = random.randint (1, 6)

                    if u_choice < 1 or u_choice > 6:
                        print("\nPlease choose a value from 1 to 6.")

                    else:
                        print("Your choice: ",u_choice, "\nComputer's choice:",c_choice)

                        if u_choice ==c_choice:
                            wickets_1 += 1

                        else:
                            if u_opt == "bat" or c_opt == "ball":
                                Bat_first = "You"

                                Ball_first = "Computer"

                                runs_1 += u_choice

                            elif u_opt =="ball" or c_opt == "bat":
                                Bat_first="Computer"
                                Ball_first="You"
                                runs_1+=c_choice
                        print("\nScore=",runs_1,"/",wickets_1)
                        balls_1 += 1

                        if balls_1 == 6:
                            print("End of Over 1")

                        elif balls_1 == 12:
                            print("End of Over 2")

                        print("Balls remaining: ",12 - balls_1)

                print("\n---------- End of First Innings ----------")

                print("\nFinal Score:")

                print("Runs =", runs_1)

                print("Wickets =",wickets_1)

                print("\n",Ball_first, "needs", runs_1 + 1, "runs to win.")

                # Second Innings
                print("\n---------- Second Innings Begins ----------")

                runs_2 = 0

                wickets_2 = 0

                balls_2 = 0

                while wickets_2 != 2 and balls_2 != 12 and runs_2 <= runs_1:
                    u_choice = int(input("\nChoose any number from 1 to 6: "))

                    c_choice=random.randint(1,6)

                    if u_choice < 1 or u_choice >6:
                        print("\nPlease choose a value from 1 to 6.")

                    else:
                        print("Your choice: ",u_choice, "\nComputer's choice: ",c_choice)

                        if u_choice == c_choice:
                            wickets_2 += 1

                        else:
                            if Bat_first == "Computer":
                                runs_2 += u_choice
                                Bat_second = "You"

                            elif Bat_first == "You":
                                runs_2 += c_choice
                                Bat_second = "Computer"

                        print("\nScore =", runs_2,"/", wickets_2)

                        balls_2 += 1

                        
                        if balls_2 == 6:
                            print("End of Over 1")

                        elif balls_2 == 12:
                            print("End of Over 2")

                        if runs_2 <= runs_1 and balls_2 <= 11 and wickets_2 != 2:
                            print("To win:", runs_1 - runs_2 + 1, "runs needed from", 12-balls_2,"balls.")

                print("\n---------- End of Second Innings ----------")

                print("\nFinal Score:")

                print("Runs =", runs_2)

                print("Wickets =", wickets_2)

                #Result of Match
                score=0
                status=""

                print("\n------- Match Result -------")

                if runs_1 > runs_2:
                    if Bat_first == "You":
                        print("\nCongratulations! You won the Match by", runs_1 - runs_2,"runs.")
                        score=runs_1
                        status="Win"
                    else:
                        print("\nBetter luck next time! The Computer won the Match by", runs_1 -runs_2,"runs.")
                        score=runs_2
                        status="Loss"

                elif runs_2> runs_1:
                    if Bat_second == "You":
                        print("\nCongratulations! You won the Match by",2- wickets_2, "wickets.")
                        score=runs_2
                        status="Win"
                    else:
                        print("\nBetter luck next time! The Computer won the Match by", 2- wickets_2, "wickets.")
                        score=runs_1
                        status ="Loss"

                else:
                    status="Tie"
                    score=runs_1
                    print("The Match is a Tie.", "\nNo one Wins.")

                # Save to database
                mycursor.execute("select * from sno")
                for i in mycursor:
                    t_id=i[0]+1
                mycursor.execute("insert into cricket values("+str(t_id)+", now(), '"+Name+"', "+str(score)+", '"+status+"')")
                mycursor.execute("update sno set id="+str(t_id))
                mydb.commit()
                print("\nMatch data saved successfully!")

    elif ch==2:
        print("""
        Instructions:

        1. You have to select any random number from 1 to 6.

        2. The computer will also select a number.

        3. While batting, if the number selected by you and computer is different, then your number will add to your runs. If the number selected by you and computer is same, then you will lose your wicket.

        4. While bowling, if the number selected by you and computer is different, then the computer's number will add to its runs.

        5. Each player will get 2 wickets and 2 overs (12 balls) for batting and bowling.

        6. The innings will end after the two wickets fell or the overs end.

        7. The player with maximum runs wins.""")

    elif ch==3:
        print("\nSNO\tDATE\t\tNAME\t\tRUNS\tSTATUS")
        print("-" * 60)
        mycursor.execute("select * from cricket")
        for i in mycursor:
            t_sno, t_date, t_name, t_run, t_status = i
            print(f"{t_sno}\t{t_date}\t{t_name}\t\t{t_run}\t{t_status}")

    elif ch==4:
        print("Thank you for playing! Goodbye!")
        break
    
    else:
        print("Invalid choice! Please select 1-4.")