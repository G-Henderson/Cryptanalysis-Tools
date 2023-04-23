class MorseTranslator():

    """
    Class for decoding ciphertexts using Morse Code
    """

    def __init__(self) -> None:
        self.morse_alphabet = {'.-': 'a', '-...': 'b', '-.-.': 'c', '-..': 'd', '.': 'e', '..-.': 'f', '--.': 'g', '....': 'h', '..': 'i', '.---': 'j', '-.-': 'k', '.-..': 'l', '--': 'm', '-.': 'n', '---': 'o', '.--.': 'p', '--.-': 'q', '.-.': 'r', '...': 's', '-': 't', '..-': 'u', '...-': 'v', '.--': 'w', '-..-': 'x', '-.--': 'y', '--..': 'z', '/': ' ', '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9'}

    def decode(self, ciphertext: str, separator: str=" ") -> str:
        """
        Function for decoding ciphertext which has been encoded using morse code.
        """

        # Create a new empty variable to store the output
        output = ""
        # Convert the string into a list
        message_list = ciphertext.split(separator)

        # Iterate through each morse character in the list
        for letter in message_list:
            # Get the equivalent plaintext character from the list and add it to the output string
            try:
                output += self.morse_alphabet[letter]
            except:
                print(f"Unable to translate '{letter}' charcter...")

        # Return the output string as all caps
        return output.upper()