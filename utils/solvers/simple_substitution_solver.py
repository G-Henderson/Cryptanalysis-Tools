from utils.cipher_solver import CipherSolver
from random import randint, shuffle

class SimpleSubSolver(CipherSolver):

    """
    Class for decrypting ciphertexts encrypted using the Simple Substitution cipher
    """

    def __init__(self) -> None:
        super().__init__()

        # Setup alphabet list
        self.ALPHABET = list(("abcdefghijklmnopqrstuvwxyz").upper())

    def with_key(self, message: str, key: str) -> str:
        """
        Function for dcecryting ciphertext from known key
        """

        # Convert the key into a list
        cipher_alphabet = list(key.upper())

        # Create empty string variable to hold decrypted message
        decrypt = ""

        # Iterate through the message
        for char in message:
            # Get the index of the cipher alphabet where the current char is located
            m_index = cipher_alphabet.index(char)

            # Get the plaintext char at that index
            plain_char = self.ALPHABET[m_index]

            # Add to the decrypt string
            decrypt += plain_char

        # Return the decrypted message
        return decrypt

    def brute_force(self, message) -> str:
        # Create random key to start with
        best_key = self.ALPHABET.copy()
        # Set the best score to really low number
        best_score = -99e9

        # Setup the parent key and score
        parent_key = best_key.copy()
        parent_score = best_score

        # Try solving 100 times
        for i in range(100):
            # Randomise the parent key
            shuffle(parent_key)
            # Decrypt using the new parent key
            decrypt = self.with_key(message, "".join(parent_key))
            # Get the fitness score for decryption as the benchmark
            parent_score = self.quadgram_scorer.ngram_score(decrypt)

            # Perform the hill climb
            iter_since_improv = 0
            while iter_since_improv < 1000:
                # Get two random indexes of letter to swap
                swap_a = randint(0,len(self.ALPHABET)-1)
                swap_b = randint(0,len(self.ALPHABET)-1)

                # Setup child key variable
                child_key = parent_key.copy()

                # Swap the letters
                child_key[swap_a], child_key[swap_b] = child_key[swap_b], child_key[swap_a]

                # Try deciphering with the child key and then score it using ngrams
                decrypt = self.with_key(message, "".join(child_key))
                child_score = self.quadgram_scorer.ngram_score(decrypt)

                # Check if it has a better fitness
                if (child_score > parent_score):
                    # Replace the parent key with the child key
                    parent_key = child_key.copy()
                    # Set the new parent score
                    parent_score = child_score
                    # Set the number of iterations since improvement back to 0
                    iter_since_improv = 0

                # Add one to the number of iterations since improvement
                iter_since_improv += 1

            # Check if this local maximum found a better decryption key
            if (parent_score > best_score):
                # Set the new best score and best key
                best_score = parent_score
                best_key = parent_key.copy()

        # Return the decrypt using the best key
        return self.with_key(message, "".join(best_key))



