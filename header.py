# Sergei Chaparin
# Joy of Coding

def header(text, surround):
    length = len(text) + 4
    decorated_string = (surround * length) + "\n" + surround + " " + text + " " + surround + "\n" + (surround * length)
    return decorated_string


def main():
    print(header("Nakupenda Mpenzi Sana", "♥️"))
    print(header("Nakupenda Mpenzi Sana", "¤"))
    print(header("Nakupenda Mpenzi Sana", "燦"))


main()
