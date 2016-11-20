import datetime


def years(age):
    age_100 = 100 - age
    result = datetime.date.today().year + age_100
    return result


def main():
    return


if __name__ == '__main__':
    main()
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    copie = int(input("Enter a number: "))
    copies = copie * (str(name) + ", you will be 100 years old in " + str(years(age)) + ".\n")
    print(copies)
