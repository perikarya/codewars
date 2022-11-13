def duplicate_count(text):
    text = text.casefold()
    unique_chars = []
    for i in text:
        if (i not in unique_chars and text.count(i) > 1):
            unique_chars.append(i) 
    return len(unique_chars)
