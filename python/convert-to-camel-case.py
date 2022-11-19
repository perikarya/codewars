def to_camel_case(text):
    splittext = text.replace("_", "-").split("-")
    capitalized = [word.capitalize() for word in splittext]
    return splittext[0] + "".join(capitalized[1:])
