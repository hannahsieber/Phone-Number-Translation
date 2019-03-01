def find_num(text):
    numbers = ["zero","one","two","three","four",
               "five","six","seven","eight","nine"]
    for i in range(0,10):
        if numbers[i] == text:
            return str(i)
    return False


def main():
    phone = "("

    input_str = input("Please enter your phone number, spelled out with spaces between words\n"
                      "Ignore the '1' at the beginning\n\n")
    input_arr = input_str.split(" ")

    while input_arr.__len__() != 10:
        input_str = input("I was expecting ten words. Try again!\n")
        input_arr = input_str.split(" ")

    digit = 0
    for word in input_arr:
        while not find_num(word):
            word = input("What did you mean by " + word + "?\n")
        phone += find_num(word)
        digit += 1
        if digit == 3:
            phone += ")"
        elif digit == 6:
            phone += "-"
    print(phone)


if __name__ == '__main__':
    main()