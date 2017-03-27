def alphabet_position(letter):
    alp = "abcdefghijklmnopqrstuvwxyz"
    upper_alp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    #letter.lower()
    if letter in alp:
        return alp.index(letter)
    else:
        return upper_alp.index(letter)

def rotate_character(char, rot):
    alp = "abcdefghijklmnopqrstuvwxyz"
    upper_alp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if char in alp or char in upper_alp:
        pos = (alphabet_position(char) + rot) % 26
        if char in alp:
            return alp[pos]
        else:
            return upper_alp[pos]

    else:
        return char
def encrypt(text, rot):
    newText = ""
    for item in text:
        newText = newText + rotate_character(item, rot)
    return newText
