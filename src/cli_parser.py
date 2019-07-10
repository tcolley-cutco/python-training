

# All arguments will appear in a dictionary
# RULES LISTED BELOW
# The command itself is the first word. It is always ignored
# Positional arguments will be given their index as the key
# All positional arguments must be before any flagged arguments or they'll be parsed incorrectly
# Flagged arguments can start with / or -
# Flagged arguments will have the flag as the key. If there's no corresponding value, it will have a blank string value
def parse_args(argv):

    i = 1
    pos_counter = 0
    arguments_are_positional = True
    current_flag = ''
    parsed_arguments = dict()

    argv_mirror = argv.copy()
    del argv_mirror[0]   # remove the leading argument because it's the program name
    for arg in argv_mirror:
        is_flag = arg.startswith("/") or arg.startswith("-")
        if is_flag:
            arguments_are_positional = False
            if current_flag != '' and current_flag not in parsed_arguments:
                parsed_arguments[current_flag] = ''
            current_flag = arg
        else:
            if arguments_are_positional:
                parsed_arguments[pos_counter] = arg
                pos_counter += 1
            else:
                if current_flag in parsed_arguments:
                    existing_value = parsed_arguments[current_flag]
                    existing_value += " " + arg
                    parsed_arguments[current_flag] = existing_value
                else:
                    parsed_arguments[current_flag] = arg
        i += 1

    if current_flag != '' and current_flag not in parsed_arguments:
        parsed_arguments[current_flag] = ''

    return parsed_arguments

