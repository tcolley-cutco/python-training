class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_nick_name(self):
        nick_name = ''
        if self.name == 'Tony':
            nick_name = 'T'
        return nick_name


test_person = Person("Tony", 21)

print(f"My nick name is {test_person.get_nick_name()} and my age is {test_person.age}.")


string_to_print = ("This is my string and it's very long, so much so that despite the fact that my name is " +
                   f"{test_person.name} and not {test_person.get_nick_name()} that this string will still exceed " +
                   "the length for a single line!")

print(string_to_print)
