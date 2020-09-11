def collatz(number):
    if number % 2 == 0:
        output = number // 2
        print(output)
        return output
    else:
        output = 3 * number + 1
        print(output)
        return output


if __name__ == '__main__':
    userInput = int(input('Enter a number:'))
    while True:
        userInput = collatz(userInput)
        if userInput == 1:
            break
