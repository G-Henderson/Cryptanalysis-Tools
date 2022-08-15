from utils.stat_measurer import StatMeasurer
from utils.ngrams_scorer import NgramScorer, NgramFiles
from utils.cipher_solver import CipherSolver

class BestList(object):

    def __init__(self, max_len=100) -> None:
        self.my_list = []
        self.max_len = max_len

    def add(self, item) -> None:
        # Add the item to the list
        self.my_list.append(item)
        # Sort the list in reverse order
        self.my_list.sort(reverse=True)
        # Remove anything not in the top N
        self.my_list = self.my_list[:self.max_len]

    def __getitem__(self, index: int):
        # Return the item at the specified index from the list
        return self.my_list[index]

    def __len__(self) -> int:
        # Return the length of the best list
        return len(self.my_list)


class VigenereSolver(CipherSolver):

    """
    Class for decrypting ciphertexts encrypted using the Vigenere cipher
    """

    def __init__(self) -> None:
        super().__init__()

        # Setup trigram scorer instances
        self.trigram_scorer = NgramScorer(NgramFiles.TRIGRAM_FILE)

        # Setup the alphabet as a final variable
        self.ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def with_key(self, message: str, key: str) -> str:
        # Initialise the variable to store the decrypted text
        decrypt = ""

        # Make sure the key is all caps
        key = key.upper()

        # Iterate through each character of the ciphertext
        for i in range(len(message)):
            decrypt += chr((((ord(message[i]) - 65) - (ord(key[i % len(key)]) - 65) + 26) % 26) + 65)

        # Return the decrypted text
        return decrypt

    def with_keylen(self, message: str, keylen: int) -> str:
        best_list = BestList()

        for i in range(keylen):
            for j in range(len(self.ALPHABET)):
                key = 

        # Return the decrypted message
        return decrypt

    def brute_force(self, message: str) -> str:
        self.get_period(message)
        return super().brute_force(message)

    def get_period(self, message: str) -> int:
        # Find the I.C's of key lengths between 2 and 15
        for a in range(2,16):
            sequences = []
            for b in range(a):
                current = ""
                more_letters = True
                index = b
                while more_letters:
                    try:
                        current += message[index]
                        index += a
                    except:
                        more_letters = False

                sequences.append(current)

            total = 0
            for b in range(len(sequences)):
                total += self.mFitTester.get_ic(sequences[b])

            average = total / len(sequences)
            print(str(a)+":  "+str(average))

        return 0

    def get_permutations(self, list_digits: list, perm_len: int=None) -> list:
        """
        Function to find all permutations of a string (that has been converted to a list)
        """

        # Check if given specific permutation length
        if (perm_len == None):
            perm_len = len(list_digits)

        # Check that there are digits to find permutations of
        if (len(list_digits) == 0):
            return []

        # Check whether only 1 permutation is possible
        elif (len(list_digits) == 1):
            return [list_digits]

        # Else find the permutations of the digits given
        else:
            # Create an empty list to store the permutations
            my_permutations = []

            # Iterate through the list
            for digit in list_digits:
                other_digits = list_digits[:list_digits.index(digit)] + list_digits[list_digits.index(digit)+1:]

                # Get all the permutations where the current digit is 1st
                for permutation in self.get_permutations(other_digits):
                    my_permutations.append([digit] + permutation)

            # Return the list of permutations
            return my_permutations