from utils.TextUtils import TextUtils

class CaesarSolver:

    """
    Class for decrypting ciphertexts encrypted using the Caesar cipher
    """

    def __init__(self) -> None:
        self.TU = TextUtils()

    def solve(self, message, shift=None):
        """
        Function for decrypting with unknown shift
        """

        # Remove anything that's not a letter
        message = self.TU.only_letters(message)

        # Make message uppercase
        message = message.upper()
        
        # Setup empty variable for containing decoded message
        decoded_msg = ""

        # Check whether the shift is known
        if (shift != None):
            for i in range(len(message)):
                char = message[i]
                decoded_msg += chr((ord(char) + shift-65) % 26 + 65)

        else:
            pass
        
        print(decoded_msg)
        return decoded_msg