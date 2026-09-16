guests = ["Adekunle", "Mariam", "Taju", "Amaka", "James", "Adekunle"]
statuses = ["confirmed", "confirmed", "pending", "confirmed", "pending", "confirmed"]
ages = [21, 22, 19, 24, 20, 22]

while True:
    print("========== MOTION GUEST MANAGER ==========")
    print("1. View all guests")
    print("2. Check confirmed guests")
    print("3. Check pending guests")
    print("4. Search for a guest")
    print("5. Add guest")
    print("6. Remove guest")
    print("7. Confirm guest")
    print("8. Cancel guest")
    print("9. Show guest statistics")
    print("0. Exit")
    print("=" * 45)

    while True:
        operation = input("Enter operation (from 0 to 9): ")
        if not operation.isdigit():
            print("Enter only Numbers!")
            print("=" * 45)
            continue
        if operation not in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
            print("invalid Numbers (numbers 0-10 only)")
            print("=" * 45)
        else:
            break

    if operation == "1":
        for index in range(len(guests)):
            print(f"{guests[index]: <10} Age: {ages[index]: >2} {" " * 2}Status: {statuses[index]} ")
        print()
        continue

    elif operation == "2":
        confirmed_guests_index = []
        for status in range(len(statuses)):
            if statuses[status].lower() == "confirmed":
                confirmed_guests_index.append(status)

        if len(confirmed_guests_index) == 0:
            print("No Confirmed Guests")
        else:
            print("=" * 45)
            print(f"{"confirmed Guests": ^10}")
            print("=" * 45)
            for index in confirmed_guests_index:
                print(f"{str(guests[index]) : <10} age: {str(ages[index]) : <10}")
                continue

    elif operation == "3":
        print("=" * 45)
        print(f"{"pending Guest": ^10}")
        print("=" * 45)
        pending_guests_index = []
        for status in range(len(statuses)):
            if statuses[status].lower() == "pending":
                pending_guests_index.append(status)

        if len(pending_guests_index) == 0:
            print("No Confirmed Guests")
        else:
            for index in pending_guests_index:
                print(f"{str(guests[index]) : <10} age: {str(ages[index]) : <10}")
                continue

    elif operation == "4":
        search_prompt = input("What are you looking for: ").capitalize()

        index_of_search_occurrence = []
        index_of_related_searches = []
        for guest_index in range(len(guests)):
            if guests[guest_index] == search_prompt:
                index_of_search_occurrence.append(guest_index)
            elif guests[guest_index][:3] == search_prompt[:3]:
                index_of_related_searches.append(guest_index)

        if len(index_of_related_searches) >= 1 and len(index_of_search_occurrence) == 0:
            print("Your search yielded no results")
            print("Here are the related results")
            for count in range(len(index_of_related_searches)):
                print(
                    f"{str(guests[index_of_related_searches[count]]): >5}{count + 1} age: {str(ages[index_of_related_searches[count]]): >5} status: {str(statuses[index_of_related_searches[count]]): >5}")

        elif len(index_of_search_occurrence) == 0 and len(index_of_related_searches) == 0:
            print("Your Search did not yield any results")
        elif len(index_of_search_occurrence) == 1:
            print(
                f"{str(guests[index_of_search_occurrence[0]]):<5} age: {str(ages[index_of_search_occurrence[0]])} status: {str(statuses[index_of_search_occurrence[0]]): >5}")
        elif len(index_of_search_occurrence) > 1:
            print("Your search yielded multiple results")
            for count in range(len(index_of_search_occurrence)):
                print(
                    f"{str(guests[index_of_search_occurrence[count]]): >5}{count + 1} age: {str(ages[index_of_search_occurrence[count]])} status: {str(statuses[index_of_search_occurrence[count]]): >5}")

    elif operation == "5":
        while True:
            guest_add = input("Enter name of guest: ").capitalize()
            if not guest_add.isalpha():
                print("name must be only alphabets")
                continue
            else:
                break
        while True:
            age_of_guest = input(f"How old is {guest_add}: ").capitalize()
            if not age_of_guest.isdigit():
                print("age is supposed to be digit only")
                continue
            elif int(age_of_guest) > 50:
                print(f"{guest_add} is too old")
                break
            elif int(age_of_guest) < 18:
                print(f"{guest_add} is too young")
                break
            else:
                while True:
                    eligibility = input("confirmed or pending: ").capitalize()
                    if eligibility not in ("Confirmed", "Pending"):
                        print("Enter Pending or confirmed")
                        continue
                    else:
                        guests.append(guest_add)
                        statuses.append(eligibility)
                        ages.append(int(age_of_guest))
                        break
                break

    elif operation == "6":
        while True:
            remove_guest = input("Who do you wanna remove from the guestlist: ").capitalize()
            if not remove_guest.isalpha():
                print("Only Alphabets are accepted here.")
                continue
            if not remove_guest in guests:
                print(f"name: {remove_guest} is not in our records")
                break

            index_of_guests = []
            for index in range(len(guests)):
                if remove_guest == guests[index]:
                    index_of_guests.append(index)

            if len(index_of_guests) == 1:
                index = index_of_guests[0]

                print(
                    f"{statuses[index]} guest with name: {remove_guest} with age:{ages[index]} has been removed from our records")
                guests.pop(index)
                ages.pop(index)
                statuses.pop(index)
                break

            if len(index_of_guests) > 1:
                print("Your Search yielded multiple Results")
                for index in range(len(index_of_guests)):
                    index_of_guest = index_of_guests[index]
                    print(
                        f"{index + 1}. {statuses[index_of_guest]} guest with name: {remove_guest} with age:{ages[index_of_guest]}")

                while True:
                    choice = input("What choice do you want to delete: ")
                    if not choice.isdigit():
                        print("Input only digits")
                        continue
                    else:
                        choice = int(choice) - 1

                        print(
                            f"{statuses[choice]} guest with name: {remove_guest} with age:{ages[choice]} has been removed from our records")
                        guests.pop(choice)
                        ages.pop(choice)
                        statuses.pop(choice)
                        break

            break

    elif operation == "7":
        print("This is the list of all pending guests")
        counter = 1
        all_pending_guests = []
        for confirmed_guests_index in range(len(statuses)):
            if statuses[confirmed_guests_index].lower() == "pending":
                print(
                    f"{counter}. {guests[confirmed_guests_index]: >5} {" " * 3} status: {statuses[confirmed_guests_index]: >5}")
                all_pending_guests.append(confirmed_guests_index)

                counter += 1
        while True:
            confirmed_guest_number = input("Which guest do you wanna confirm: ")
            if not confirmed_guest_number.isdigit():
                print("only numbers are allowed")
                continue
            elif len(all_pending_guests) < int(confirmed_guest_number):
                print("invalid number: pick the numbers available above")
                continue
            else:
                break
        index = all_pending_guests[int(confirmed_guest_number) - 1]
        statuses[index] = "confirmed"
        print(f"{guests[index]} has been successfully confirmed")

    elif operation == "8":
        print("This is the list of all Confirmed guests")
        counter = 1
        all_confirmed_guests = []
        for pending_guests_index in range(len(statuses)):
            if statuses[pending_guests_index].lower() == "confirmed":
                print(
                    f"{counter}. {guests[pending_guests_index]: >5} {" " * 3} status: {statuses[pending_guests_index]: >5}")
                all_confirmed_guests.append(pending_guests_index)

                counter += 1
        while True:
            unconfirm_guest_number = input("Which guest do you wanna unconfirm: ")
            if not unconfirm_guest_number.isdigit():
                print("only numbers are allowed")
                continue
            elif len(all_confirmed_guests) < int(unconfirm_guest_number):
                print("invalid number: pick the numbers available above")
                continue
            else:
                break
        index = all_confirmed_guests[int(unconfirm_guest_number) - 1]
        statuses[index] = "pending"
        print(f"{guests[index]} has been successfully cancelled")

    elif operation == "9":
        print("Guest statistics")
        print("=" * 45)

        number_of_confirmed_guests = 0
        number_of_unconfirmed_guests = 0
        sum_of_all_guests_ages = 0
        for count in range(len(statuses)):
            if statuses[count].lower() == "confirmed":
                number_of_confirmed_guests += 1
            else:
                number_of_unconfirmed_guests += 1

        for age in ages:
            sum_of_all_guests_ages += age

        average_age_of_guests = int(sum_of_all_guests_ages / len(ages))

        print(f"PERCENTAGE OF CONFIRMED GUESTS: {int((number_of_confirmed_guests / len(statuses)) * 100): >5}% \n"
              f"PERCENTAGE OF UNCONFIRMED GUESTS: {int((number_of_unconfirmed_guests / len(statuses)) * 100): >5}%\n"
              f"NUMBER OF GUESTS: {len(guests): >5}\n"
              f"AVERAGE AGE OF GUESTS: {average_age_of_guests: >5}")
        

    elif operation == "0":
        print("Thanks for buying with us")
        break
    