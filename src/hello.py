import sys


def find_age(age_string):
    age = ''
    for char in age_string:
        if char.isnumeric():
            age = age + char

    return age


def main():
    print("Hello world!")

    # Step 2
    calculated_number = 11 * 2

    # Step 3
    float_number = 1.618

    # Step 4
    my_string = "My age is "

    # Step 5
    age_string = my_string + "40 years old"

    # Step 6
    print("%s and 2 months" % age_string)
    print("%d is my favorite float as a decimal" % float_number)
    print("%f is my favorite float" % float_number)

    # Step 7
    print("%s %d years old" % (my_string, calculated_number))

    # 8. Try adding a float number to the print statement
    # We needed to cast the float to a string so Python would print it
    print("Let's print a float: " + str(float_number))

    # 9. Try appending an integer to a string. What happens?
    # It doesn't work because Python doesn't let you cross the wires like that
    # This can be worked by adding a string cast.
    concat_string = str(1) + "1"
    print("Let's print a concatenated string!" + concat_string)

    # Moving on to part C

    # Step 3
    str_len = len(age_string)
    print(str_len)

    # Step 4
    index_of = age_string.index("e")
    print(index_of)

    # Step 5
    sub_string = age_string[2:4]
    print(sub_string)

    # Step 6
    upper_string = age_string.upper()
    print(upper_string)
    lower_string = age_string.lower()
    print(lower_string)

    # 7. Try using substring to extract age is from age_string
    age = find_age(age_string)
    print(age)

    # 8. Try finding the index of the word years. The index
    # is the starting position of the value found
    print(age_string.index("years"))

    # Time to start part D
    print("All arguments to program listed below!")
    for arg in sys.argv:
        print(arg)


main()
sys.exit(0)
