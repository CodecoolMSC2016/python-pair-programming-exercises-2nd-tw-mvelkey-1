def fizzbuzz(number):
    counter = 0
    for i in number:
        if int(i) % 3 == 0 and int(i) % 5 == 0:
            number[counter] = "FizzBuzz"
            counter += 1
        elif int(i) % 3 == 0:
            number[counter] = "Fizz"
            counter += 1
        elif int(i) % 5 == 0:
            number[counter] = "Buzz"
            counter += 1
        else:
            number[counter] = int(i)
            counter += 1
    return number


def main():
    for i in range(1, 101):
        number.append(str(i))
    return number


if __name__ == '__main__':
    number = []
    main()
    print(fizzbuzz(number))