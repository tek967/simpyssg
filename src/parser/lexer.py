"""
Lexer for markdown flavor.
"""

def round_1(text: str) -> list:
    " round 1 of lex "

    result = []
    text_loc_log = [0]
    done = False
    ptr = 0

    while not done:
        if ptr >= len(text)-1:
            done=True
            result.append(text[text_loc_log[len(text_loc_log)-1]:len(text)])
        if text[ptr] == "*" or text[ptr] == "_":
            if text[ptr+1] == "*" or text[ptr+1] == "_":
                if text[ptr+2] == "*" or text[ptr+1] == "_":
                    result.append(text[text_loc_log[len(text_loc_log)-1]:ptr])
                    result.append("***")
                    text_loc_log.append(ptr+3)
                    ptr += 3
                else:
                    result.append(text[text_loc_log[len(text_loc_log)-1]:ptr])
                    result.append("**")
                    text_loc_log.append(ptr+2)
                    ptr += 2
            else:
                result.append(text[text_loc_log[len(text_loc_log)-1]:ptr])
                result.append("*")
                text_loc_log.append(ptr+1)
                ptr += 1
        else:
            ptr += 1
    return result

def check_if_all_whitespaces(string: str) -> bool:
    " check if all whitespaces "

    print(string)
    for char in string:
        if char != " ":
            return False
    return True

def round_2(text: list) -> list:
    "lexer pass 2"

    retval = []
    for count, char in enumerate(text[0]):
        print(f"loop {char}")
        if (char == "#" and text[0][count+1] == " ") or char == " ":
            try:
                all_ws = check_if_all_whitespaces(text[0][:count])
            except IndexError:
                all_ws = True

            if all_ws:
                print("detected heading 1")
                retval.append("# ")
                retval.append(text[0][count+2:len(text[0])])
                break

    return retval

def lex(text: list) -> list:
    " Glue function for lexer "

    # round 1: analyze for basic text markup.
    retval = []
    for line in text:
        retval.append(round_1(line))

    # round 2: analyze for titles and headings.

    return retval

if __name__ == "__main__":
    print(lex(['first line* arstarsytl*hoyalwffp\n', '\n', 'second line arst**ylh**wfd\n', 'third *l*ine arsytlohq34***08ul***ioh\n', '\n', 'fourth line ar***ol***dh24q34h;y8\n']))
