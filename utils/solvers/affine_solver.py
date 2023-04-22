from utils.cipher_solver import CipherSolver

class AffineSolver(CipherSolver):

    """
    Class for decrypting ciphertexts encrypted using the Affine cipher
    """

    def __init__(self) -> None:
        super().__init__()

    def with_key(self, message: str, key: tuple) -> str:
        # Get separate keys
        if (type(key) == tuple):
            if (len(key) >= 2):
                # Get key a and b from the tuple
                a = int(key[0])
                b = int(key[1])

                output = ""
                modInverseOfKeyA = pow(a, -1, len(self.ALPHABET))
                for i in range(len(message)):
                    index = self.ALPHABET.index(message[i])
                    output += self.ALPHABET[(index - b) * modInverseOfKeyA % len(self.ALPHABET)]

                return output

            else:
                # Throw an error
                raise Exception("Affine solver: 2 keys are required!")

        else:
            # Throw an error
            raise Exception("Affine solver: a tuple of 2 keys is required!")

    def brute_force(self, message: str) -> str:
        best_score = -99e9
        best_msg = ""
        for b in range(25):
            for a in [1,3,5,7,9,11,15,17,19,21,23,25]:
                # Get the decrypted message
                curr_msg = self.with_key(message, (a, b))

                # Get a score for that message
                curr_score = self.quadgram_scorer.ngram_score(curr_msg)

                # Check if score is better than previous best
                if (curr_score > best_score):
                    # Update the best score and best message
                    best_score = curr_score
                    best_msg = curr_msg

        # Return the highest scoring message text
        return best_msg