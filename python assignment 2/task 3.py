
# Q3 - Vehicle Registration Number Validator

def normalise(text):
    text = text.replace(" ", "")
    text = text.replace("-", "")
    return text.upper()


def is_valid(reg):
    if len(reg) not in (9, 10):
        return False

    if not reg[0:2].isalpha():
        return False

    if not reg[2:4].isdigit():
        return False

    if len(reg) == 9:
        if not reg[4:5].isalpha():
            return False
        if not reg[5:9].isdigit():
            return False

    else:
        if not reg[4:6].isalpha():
            return False
        if not reg[6:10].isdigit():
            return False

    return True


def format_number(reg):
    reg = normalise(reg)

    if not is_valid(reg):
        return "Invalid number"

    if len(reg) == 9:
        return reg[:2] + " " + reg[2:4] + " " + reg[4:5] + " " + reg[5:]

    return reg[:2] + " " + reg[2:4] + " " + reg[4:6] + " " + reg[6:]


number = input("Enter vehicle number: ")

reg = normalise(number)

if is_valid(reg):
    print("Valid number")
    print("Formatted number:", format_number(reg))
else:
    print("Invalid number")
