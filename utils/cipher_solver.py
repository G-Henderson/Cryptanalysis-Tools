from utils.TextUtils import TextUtils
from utils.FitnessTest import FitnessTest

class CipherSolver():

    """
    Template class for decrypting ciphertexts
    """

    def __init__(self) -> None:
        self.TU = TextUtils()
        self.mFitTester = FitnessTest()

    def solve(self, message: str, key=None, keylen: int=None) -> str:
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
            decoded_msg = self.with_key(message, key)

        # Check whether we're given a key length
        elif (keylen != None):
            # Try decoding the message with the known key length
            decoded_msg = self.with_keylen(message, keylen)

        else:
            # Try solving the cipher using brute force
            decoded_msg = self.brute_force(message)

        return decoded_msg

    def with_key(self, message: str, key) -> str:
        return ""

    def with_keylen(self, message: str, keylen: int) -> str:
        return ""

    def brute_force(self, message: str) -> str:
        return ""