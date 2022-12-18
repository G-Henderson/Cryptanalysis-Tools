from utils.cipher_solver import CipherSolver

class CaesarSolver(CipherSolver):

    """
    Class for decrypting ciphertexts encrypted using the Playfair cipher
    """

    def __init__(self) -> None:
        super().__init__()

    def with_key(self, message: str, alphabet: int) -> str:
        output = ""
        

        return output

    def brute_force(self, message: str) -> str:
        best_score = -99e9
        best_msg = ""
        for shift in range(1,26):
            # Get the shifted message
            curr_msg = self.with_key(message, shift)

            # Get a score for that message
            curr_score = self.quadgram_scorer.ngram_score(curr_msg)

            # Check if score is better than previous best
            if (curr_score > best_score):
                # Update the best score and best message
                best_score = curr_score
                best_msg = curr_msg

        return best_msg