import csv

file_create = open("DataBase.csv", "w")
ADMIN = "admin, admin \n"
file_create.write(str(ADMIN))
file_create.close()


def main():
    """
    The function of creating a menu for communication with the program.

    :return:
    """
    start = int(input("""
        1) Create a new User ID
        2) Change a password
        3) Display all User IDs
        4) Quit
        Enter Selection: """))
    if start == 1:
        create_user()
    elif start == 2:
        change_password()
    elif start == 3:
        display_all_users()
    elif start == 4:
        print("See you letter!")
        quit()
    else:
        print("Try again!")
        main()


def create_user():
    """
    The code block is fully responsible for registering a new user.
    Two nested functions are responsible for collecting information from the user and
    also conducting tests required for registration.
    They return one line at a time,which at the end of the block will be needed to group information and
    add a user to the database.

    :return:
    """

    def user_id_create():
        """
        The first stage during registration and checking the user ID for the presence of a clone.

        :return:
        """
        new_user_id = input("Enter new user ID: ")
        file_checker = open("DataBase.csv", "r")  # UPGRADE...
        for row in file_checker:
            if new_user_id in row:
                print("Sorry but user ID busy!")
                create_user()
            else:
                return new_user_id

    def user_password_create():
        """
        The second stage of user registration, requesting a password,
        checking its reliability and complexity through five tests.
        - length.
        - presence of symbols.
        - presence of number.
        - uppercase letters.
        - lowercase letters.

        :return:
        """
        while True:
            new_user_password = input("Enter new password: ")
            list_password = []
            list_symbol = ["!", "£", "$", "%", "&", "<", "*", "@"]

            # Password placed in checklist.
            for i in new_user_password:
                list_password.append(i)

            # Tests starting.
            check_len = len(new_user_password) > 7
            check_sym = set(list_password) & set(list_symbol)
            check_num = False
            check_upp = False
            check_low = False

            for i in new_user_password:
                if i.isupper():
                    check_upp = True
            for i in new_user_password:
                if i.islower():
                    check_low = True
            for i in new_user_password:
                if i.isdigit():
                    check_num = True

            password_lvl = 0

            if check_len:
                password_lvl += 1
            if check_num:
                password_lvl += 1
            if check_sym:
                password_lvl += 1
            if check_upp:
                password_lvl += 1
            if check_low:
                password_lvl += 1

            # Result.
            if password_lvl == 5:
                print(f"You are well done, this is a strong password! LVL{password_lvl}")
                return new_user_password
            elif password_lvl == 3 or password_lvl == 4:
                improve = input(
                    f"This is an average password LVL{password_lvl} and can be improved, would you like to do this? (y/n): ")
                improve.islower()
                if improve == "y":
                    continue  # To the beginning of the cycle.
                elif improve == "n":
                    return new_user_password
                else:
                    print("ERROR")
                    continue  # Beginning of cycle.
            elif password_lvl == 1 or password_lvl == 2:
                print(f"Password is too weak, LVL{password_lvl} please try again!")
                continue  # Beginning of cycle.
            else:
                print("""ERROR\nTry again!""")
                continue  # Beginning of cycle.

    # Calls two sub-functions that provide information to add to the database.
    result = f"{user_id_create()}, {user_password_create()}\n"
    file_add = open("DataBase.csv", "a")
    file_add.write(str(result))  # UPGRADE...
    file_add.close()
    print(f"User {result.split(',')[0]} was added!")
    main()


def change_password():
    """
    The block responsible for changing the password,
    provided that the user ID is present in the database.

    :return:
    """
    file = list(csv.reader(open("DataBase.csv")))  # UPGRADE...
    userID = input("Enter ID: ")
    tmp = []

    for row in file:
        tmp.append(row)

    for row in tmp:
        if userID in row:  # User ID verification...
            confirmation = input("User valid! Do you want continue? (y/n): ")
            confirmation.islower()
            if confirmation == "y":
                new_password = (input("Enter new password: "))
                tmp.remove(row)  # Del old history.
                new_info = [userID, new_password]  # Union info.
                tmp.append(new_info)  # Add new info.
                print(f"Password change COMPLETE, for user '{userID}'")
            elif confirmation == "n":
                print("Okay, bye.")
                main()
            else:
                print("ERROR...")
                again = input("Do you want tru again? (y/n): ")
                again.islower()
                if again == "y":
                    change_password()
                else:
                    main()
        else:
            print("User ID invalid!")
            main()

            # Adding change password in database.
            file_change = open("DataBase.csv", "w")  # UPGRADE...
            x = 0
            for _ in tmp:
                newRec = tmp[x][0] + ", " + tmp[x][1] + '\n'
                file_change.write(newRec)
                x += 1
            file_change.close()
            main()


def display_all_users():
    """
    The function displays all users in the database.

    :return:
    """
    file = open("DataBase.csv", "r")  # UPGRADE...
    reader = csv.reader(file, delimiter=",")
    count = 0
    for row in reader:
        print(f'{row[0]}')
        count += 1
    print("\n"f"{count} users in total. ")
    main()


main()
