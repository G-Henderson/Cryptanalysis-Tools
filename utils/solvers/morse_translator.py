
class MorseTranslator():

    """
    Class for decrypting ciphertexts and encrypting plaintexts using Morse Code
    """

    def __init__(self) -> None:
        self.morse_alphabet = {'.-': 'a', '-...': 'b', '-.-.': 'c', '-..': 'd', '.': 'e', '..-.': 'f', '--.': 'g', '....': 'h', '..': 'i', '.---': 'j', '-.-': 'k', '.-..': 'l', '--': 'm', '-.': 'n', '---': 'o', '.--.': 'p', '--.-': 'q', '.-.': 'r', '...': 's', '-': 't', '..-': 'u', '...-': 'v', '.--': 'w', '-..-': 'x', '-.--': 'y', '--..': 'z', '/': ' '}
        self.normal_alphabet = {"a":".-", "b":"-...", "c":"-.-.", "d":"-..", "e":".", "f":"..-.", "g":"--.", "h":"....", "i":"..", "j":".---", "k":"-.-", "l":".-..", "m":"--", "n":"-.", "o":"---", "p":".--.", "q":"--.-", "r":".-.", "s":"...", "t":"-", "u":"..-", "v":"...-", "w":".--", "x":"-..-", "y":"-.--", "z":"--..", " ": "/"}

    def decode(self, ciphertext: str, separator: str=" ") -> str:
        # Create a new empty variable to store the output
        output = ""
        # Convert the string into a list
        message_list = ciphertext.split(separator)

        # Iterate through each morse character in the list
        for letter in message_list:
            # Get the equivalent plaintext character from the list and add it to the output string
            output += self.morse_alphabet[letter]

        # Return the output string as all caps
        return output.upper()

    def encode(self, plaintext: str) -> str:
        # Create a new empty variable to store the output
        output = ""

        # Iterate through each morse character in the message
        for letter in plaintext.lower():
            # Get the equivalent plaintext character from the list and add it to the output string
            output += f"{self.normal_alphabet[letter]} "

        return output