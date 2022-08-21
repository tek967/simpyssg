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
        print(ptr)
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

def lex(text: list) -> list:
    # round 1: analyze for basic text markup.
    retval = []
    for line in text:
        retval.append(round_1(line))
    return retval

if __name__ == "__main__":
    print(lex(['first line* arstarsytl*hoyalwffp\n', '\n', 'second line arst**ylh**wfd\n', 'third *l*ine arsytlohq34***08ul***ioh\n', '\n', 'fourth line ar***ol***dh24q34h;y8\n']))


