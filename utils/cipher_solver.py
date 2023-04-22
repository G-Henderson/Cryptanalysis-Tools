from utils.TextUtils import TextUtils
from utils.ngrams_scorer import NgramScorer, NgramFiles
from utils.stat_measurer import StatMeasurer

class CipherSolver():

    """
    Template class for decrypting ciphertexts
    """

    def __init__(self) -> None:
        self.TU = TextUtils()
        self.quadgram_scorer = NgramScorer(NgramFiles.QUADGRAM_FILE) # Default to using quadgrams
        self.stat_measurer = StatMeasurer() # Setup statistics measuring class
        self.ALPHABET = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ") # Define alphabet as list

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
        return "Error: Solving with key unavailable..." # Default return message

    def with_keylen(self, message: str, keylen: int) -> str:
        return "Error: Solving with key length unavailable..." # Default return message

    def brute_force(self, message: str) -> str:
        return "Error: Solving by brute force unavailable..." # Default return message
    
    def get_permutations(self, list_chars: list) -> list:
        """
        Function to find all permutations of a string (that has been converted to a list)
        """

        # Check that there are digits to find permutations of
        if (len(list_chars) == 0):
            return []

        # Check whether only 1 permutation is possible
        elif (len(list_chars) == 1):
            return [list_chars]

        # Else find the permutations of the digits given
        else:
            # Create an empty list to store the permutations
            my_permutations = []

            # Iterate through the list
            for char in list_chars:
                other_digits = list_chars[:list_chars.index(char)] + list_chars[list_chars.index(char)+1:]

                # Get all the permutations where the current digit is 1st
                for permutation in self.get_permutations(other_digits):
                    my_permutations.append([char] + permutation)

            # Return the list of permutations
            return my_permutations