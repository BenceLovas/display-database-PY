import queries


def print_query(data):
    for i in data:
        print(*i)


def main():
    while True:
        user_input = int(input("Enter a number: "))
        if user_input == 1:
            print_query(queries.full_name())
        elif user_input == 2:
            print_query(queries.all_nick_from_miskolc())
        elif user_input == 3:
            print_query(queries.carol_full_name())
        elif user_input == 4:
            print_query(queries.another_girl())
        elif user_input == 5:
            print_query(queries.new_applicant())
        elif user_input == 6:
            print_query(queries.update_phone_number())
        elif user_input == 7:
            queries.delete_friends()
        elif user_input == 0:
            break

if __name__ == "__main__":
    main()