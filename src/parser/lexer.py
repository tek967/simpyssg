"""
Lexer for markdown flavor.
"""

class ItalicText():
    " class for italic text "
    pass

class BoldText():
    " class for bold text "
    pass

class BoldAndItalicText():
    " class for bold and italic text "
    pass

def round_1(text: str) -> list(str):
    " round 1 of lex "

    result = []
    text_loc_log = [0]

    for ptr in range(len(text)):
        if text[ptr] == "*" or text[ptr] == "_":
            if text[ptr+1] == "*" or text[ptr] == "_":
                if text[ptr+2] == "*" or text[ptr] == "_":
                    result.append(text[text_loc_log[len(text_loc_log)]:ptr-1], "***")
                    text_loc_log.append(ptr+3)
                else:
                    result.append(text[text_loc_log[len(text_loc_log):ptr-1]], "**")
                    text_loc_log.append(ptr+2)
            else:
                result.append(text[text_loc_log[len(text_loc_log)-1]:ptr-1], "*")
                text_loc_log.append(ptr+1)

    return result

def lex(text: list(str)):
    # round 1: analyze for basic text markup.
    retval = []
    for line in text:
        retval.append(round_1(line))
