def palindrome(string_input):
    string_input_rep = string_input.replace(" ", "")
    palindrom_lower = string_input_rep.lower()
    palindrome_lower_palindrome = palindrom_lower[::-1]
    if palindrom_lower == palindrome_lower_palindrome:
        print("Palindrome.")
        return True
    else:
        print("Not palindrome.")
        return False
def main():
    return


if __name__ == '__main__':
    string_input = str(input("Enter a string: "))
    main()
    palindrome(string_input)
