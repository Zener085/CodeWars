def to_camel_case(text):
    i = 0
    while i < len(text):
        if text[i] in ('-', '_'):
            text = text[:i] + text[i + 1].upper() + text[i+2:]
        else:
            i += 1

    return text