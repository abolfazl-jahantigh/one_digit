def single_digit():
    while True:
        try:
            number = int(input(" please enter your num"))
            if number < 0:
                print("please enter a positive number.")
                continue
            if number < 10:
                print(f"number is already a digit: {number}. Exiting the program.")
                return

            break
        except ValueError:
            print("please enter a valid number")

    while number >= 10:
        number = sum(int(digit) for digit in str(number))

    print(f"The single digit is: {number}")

single_digit()