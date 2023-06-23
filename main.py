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
    """
    Converts a word into its corresponding Morse code representation.

    Args:
        word_to_convert (str): The word to be converted to Morse code.
        morse_code (dict, optional): A dictionary containing the mapping of letters to Morse code.
            If not provided, the default 'code' dictionary is used.

    Returns:
        str: The Morse code representation of the input word.

    Examples:
        >>> convert_word('HELLO')
        '.... . .-.. .-.. ---'

        >>> convert_word('WORLD', {'W': '.--', 'O': '---', 'R': '.-.', 'L': '.-..', 'D': '-..'})
        '.-- --- .-. .-.. -..'
    """
    if morse_code is None:
        morse_code = code
    converted_word = ""
    for letters in word_to_convert:
        converted_word += morse_code[letters]
    return converted_word


print(f"{word} in morse code is {convert_word(word)} in morse code.")

# using lambda function
convert_word_2 = lambda word_to_convert: ' '.join(code[letter] for letter in word_to_convert)
morse_code_2 = convert_word_2(word)
print(f"{word} in Morse code is: {morse_code_2}")



