def count_unique_codes(words):
    morse_base = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---",

                  "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-",

                  "..-", "...-", ".--", "-..-", "-.--", "--.."]
    spisok = 'abcdefghijklmnopqrstuvwxyz'
    morse_dict = dict(zip(spisok, morse_base))
    morse_words = []
    for word in words:
        morse_word = ''
        for letter in word:
            morse_word += morse_dict[letter]
        morse_words += [morse_word]
    return len(set(morse_words))
if __name__ == "__main__":
    print(count_unique_codes(["gin", "zen", "gig", "msg"]))