COLOUR_CODES = {"aliceblue": "#f0f8ff", "antiquewhite": "#faebd7",
                "beige": "#f5f5dc", "black": "#000000",
                "cornflowerblue": "#6495ed", "darkgoldenrod": "#b8860b",
                "darkgreen": "#006400", "darkorange": "#ff8c00",
                "darkorchid": "#9932cc", "purple": "#a020f0"}

colour = input("Enter colour: ").lower().replace(" ", "")
while colour != "":
    if colour in COLOUR_CODES:
        print(colour, "is", COLOUR_CODES[colour])
    else:
        print("Invalid colour")
    colour = input("Enter colour: ").lower().replace(" ", "")
