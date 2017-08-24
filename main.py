import queries

MENU_OPTIONS = ["Mentors' name",
                "Nick names from Miskolc",
                "Carol's last name/phone number",
                "Who's hat?", "Add new applicant",
                "Change Jemina's phone number",
                "Delete Arsenios"]


def print_query(data):
    for i in data:
        print(*i)


def print_menu(option_list):
    for i in range(1, len(option_list)+1):
        print(i, "- " + option_list[i-1])


def menu():
    while True:
        user_input = input("Enter a number: ")
        if user_input == "1":
            print_query(queries.full_name())
        elif user_input == "2":
            print_query(queries.all_nick_from_miskolc())
        elif user_input == "3":
            print_query(queries.carol_full_name())
        elif user_input == "4":
            print_query(queries.another_girl())
        elif user_input == "5":
            print_query(queries.new_applicant())
        elif user_input == "6":
            print_query(queries.update_phone_number())
        elif user_input == "7":
            queries.delete_friends()
        elif user_input == "0":
            break
        else:
            print("Wrong input.")


def main():
    print_menu(MENU_OPTIONS)
    menu()

if __name__ == "__main__":
    main()