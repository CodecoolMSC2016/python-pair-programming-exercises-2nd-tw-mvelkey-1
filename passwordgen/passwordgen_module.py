import random

def passwordgen():
    characters = [["abcdefghijklmnopqrstuvwxyz"], ["ABCDEFGHIJKLMNOPQRSTUVWXYZ"], ["0123456789"], ["!@#$%^&*()?"]]
    password = ""
    for i in range(8):
        rand = random.randrange(0, 2)
        index_len = len(characters[rand][0])
        rand_letter = random.choice(characters[rand][0][random.randint(0, (index_len)-1)])
        password += rand_letter
        rand = random.randrange(2, 4)
        index_len = len(characters[rand][0])
        rand_letter = random.choice(characters[rand][0][random.randint(0, (index_len)-1)])
        password += rand_letter
    print(password)
    return password


def main():
    return


if __name__ == '__main__':
    main()
    passwordgen()
