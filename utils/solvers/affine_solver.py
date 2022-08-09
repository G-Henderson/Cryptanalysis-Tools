from utils.TextUtils import TextUtils
from utils.FitnessTest import FitnessTest

class AffineSolver:

    """
    Class for decrypting ciphertexts encrypted using the Affine cipher
    """

    def __init__(self) -> None:
        self.TU = TextUtils()
        self.mFitTester = FitnessTest()

        # Define alphabet
        self.ALPHABET = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    def solve(self, message, a=None, b=None) -> str:
        """
        Function for decrypting caesar ciphers
        """

        # Remove anything that's not a letter
        message = self.TU.only_letters(message)

        # Make message uppercase
        message = message.upper()
        
        # Setup empty variable for containing decoded message
        decoded_msg = ""

        # Check whether the key is known
        if (a != None) and (b != None):
            # Decode the message using the known key
            decoded_msg = self.decrypt_with_key(message, a, b)

        else:
            # Try solving the cipher using brute force
            decoded_msg = self.brute_force(message)

        return decoded_msg

    def decrypt_with_key(self, message, a, b) -> str:
        output = ""
        modInverseOfKeyA = pow(a, -1, len(self.ALPHABET))
        for i in range(len(message)):
            index = self.ALPHABET.index(message[i])
            output += self.ALPHABET[(index - b) * modInverseOfKeyA % len(self.ALPHABET)]

        return output

    def brute_force(self, message) -> str:
        best_score = -99e9
        best_msg = ""
        for b in range(25):
            for a in [1,3,5,7,9,11,15,17,19,21,23,25]:
                # Get the decrypted message
                curr_msg = self.decrypt_with_key(message, a, b)

                # Get a score for that message
                curr_score = self.mFitTester.ngram_score(curr_msg)

                # Check if score is better than previous best
                if (curr_score > best_score):
                    # Update the best score and best message
                    best_score = curr_score
                    best_msg = curr_msg

        return best_msg