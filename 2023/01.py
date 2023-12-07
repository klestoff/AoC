def get_number(text: str):
    new_s = [text[i] for i in range(len(text)) if '0' <= text[i] <= '9']
    return int(new_s[0] + new_s[-1])


def get_number_2(text: str):
    _mapping = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    new_s = ""
    i = 0
    while i < len(text):
        if '0' <= text[i] <= '9':
            new_s += text[i]
        else:
            for key in _mapping.keys():
                if key == text[i:i+len(key)]:
                    new_s += _mapping[key]
                    break
        i += 1

    print(text.rstrip() + ' -> ' + new_s)
    return int(new_s[0] + new_s[-1])


with open("01.txt", "r") as txt:
    _sum = sum([get_number_2(line) for line in txt])
    print(_sum)
