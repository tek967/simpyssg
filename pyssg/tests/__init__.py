"playground"

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
                retval.append(text[0][int(text[0].find("#"))+2:len(text[0])])
                return retval
        elif char != "#" and char != " ":
            return text

if __name__ == "__main__":
    print(round_2([" a  # hello"]))
