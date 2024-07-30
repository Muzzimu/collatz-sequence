def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1

def main():
    try:
        number = int(input("Enter an integer: "))
        while number != 1:
            number = collatz(number)
            print(number)
    except ValueError:
        print("Please enter a valid integer.")

main()
