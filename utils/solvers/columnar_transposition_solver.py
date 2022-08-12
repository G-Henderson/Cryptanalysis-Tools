from utils.TextUtils import TextUtils
from utils.FitnessTest import FitnessTest

class ColumnarTranspositionSolver:

    """
    Class for decrypting ciphertexts encrypted using the Caesar cipher
    """

    def __init__(self) -> None:
        self.TU = TextUtils()
        self.mFitTester = FitnessTest()

    def solve(self, message, pattern=None) -> str:
        """
        Function for decrypting caesar ciphers
        """

        # Remove anything that's not a letter
        message = self.TU.only_letters(message)

        # Make message uppercase
        message = message.upper()
        
        # Setup empty variable for containing decoded message
        decoded_msg = ""

        # Check whether the shift is known
        if (pattern != None):
            # Decode the message using the known shift
            pass

        else:
            # Try solving the cipher using brute force
            pass

        return decoded_msg