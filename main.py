code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.',
    ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-',
    '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ': '/'
}

word = input("Enter a word: ").upper().strip()


def convert_word(word_to_convert, morse_code=None):
    if morse_code is None:
        morse_code = code

    try:
        return ' '.join(morse_code[letter] for letter in word_to_convert)
    except KeyError:
        return "Invalid character in the input"

print(f"{word} in morse code is: {convert_word(word)}")

# using lambda function
# convert_word_lambda = lambda word_to_convert: ' '.join(code.get(letter, ' ') for letter in word_to_convert)
# print(f"{word} in Morse code is: {convert_word_lambda(word)}")

