"""
CP1404/CP5632 Practical
HEX COLOURS in a dictionary
File needs reformatting
"""


CODE_TO_NAME = {"aliceblue": "#f0f8ff", "antiquewhite": "#faebd7", "darkslategray": "#2f4f4f",
                "darksalmon": "#e9967a", "darkorchid": "#9932cc", "darkorange": "#ff8c00",
                "darkgreen": "#006400",
                "cornflowerblue": "#6495ed",
                "chocolate": "#d2691e",
                "cadetblue": "CadetBlue"}
print(CODE_TO_NAME)

colour_name = input("Enter colours name: ")
while colour_name != "":
    state_code_low = colour_name.lower()
    if colour_name in CODE_TO_NAME:
        print(colour_name, "is", CODE_TO_NAME[state_code_low])
    elif len(state_code_low) == 0:
        exit(0)
    else:
        print("Invalid colours name")
    colour_name = input("Enter colours name: ")
