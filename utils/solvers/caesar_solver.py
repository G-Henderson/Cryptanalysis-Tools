from utils.TextUtils import TextUtils
from utils.FitnessTest import FitnessTest

class CaesarSolver:

    """
    Class for decrypting ciphertexts encrypted using the Caesar cipher
    """

    def __init__(self) -> None:
        self.TU = TextUtils()
        self.mFitTester = FitnessTest()

    def solve(self, message, shift=None) -> str:
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
        if (shift != None):
            # Decode the message using the known shift
            decoded_msg = self.perform_shift(message, shift)

        else:
            # Try solving the cipher using brute force
            decoded_msg = self.brute_force(message)

        return decoded_msg

    def perform_shift(self, message, shift) -> str:
        output = ""
        for i in range(len(message)):
            char = message[i]
            output += chr((ord(char) + shift-65) % 26 + 65)

        return output

    def brute_force(self, message) -> str:
        best_score = -99e9
        best_msg = ""
        for shift in range(1,26):
            # Get the shifted message
            curr_msg = self.perform_shift(message, shift)

            # Get a score for that message
            curr_score = self.mFitTester.ngram_score(curr_msg)

            # Check if score is better than previous best
            if (curr_score > best_score):
                # Update the best score and best message
                best_score = curr_score
                best_msg = curr_msg

        return best_msg