def do_transcribe(lang):
    from .convert import convert_to_braille
    from .convert import convert_to_lang
    
    fromfile = open("sample_text.txt", "r", encoding="utf8")
    string1 = fromfile.read()
    string1 = convert_to_braille(string1, lang)
    string2 = convert_to_lang(string1, lang)

    with open("transcribed.txt", "wb") as out:
        out.write(str(string1 + " \t-\t " + string2 + "\n").encode("utf8"))
    return


def display_transcribed():
    f = open("transcribed.txt", "r", encoding="utf8")
    return f.read()
