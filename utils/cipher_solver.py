from utils.TextUtils import TextUtils
from utils.FitnessTest import FitnessTest

class CipherSolver:

    """
    Template class for decrypting ciphertexts
    """

    def __init__(self) -> None:
        self.TU = TextUtils()
        self.mFitTester = FitnessTest()

    def solve(self, message, key=None) -> str:
        """
        Function for decrypting the cipher
        """

        # Remove anything that's not a letter
        message = self.TU.only_letters(message)

        # Make message uppercase
        message = message.upper()
        
        # Setup empty variable for containing decoded message
        decoded_msg = ""

        # Check whether the shift is known
        if (key != None):
            # Decode the message using the known key
            decoded_msg = self.manually(message, key)

        else:
            # Try solving the cipher using brute force
            decoded_msg = self.brute_force(message)

        return decoded_msg

    def manually(self, message, key):
        return ""

    def brute_force(self, message):
        return ""