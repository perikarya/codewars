def alphabet_position(text):
    positions = [str(ord(i) - 96) for i in text.lower() if i.isalpha()]
    return " ".join(positions)
