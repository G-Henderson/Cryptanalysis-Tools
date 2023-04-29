from utils.cipher_solver import CipherSolver

class RailfenceSolver(CipherSolver):

    """
    Class for decrypting ciphertexts encrypted using the Rail Fence cipher
    """

    def __init__(self) -> None:
        # Initialise the super class
        super().__init__()

    def with_key(self, message: str, num_rails: int) -> str:
        """
        Function to decrypt the cipher given the number of rails
        """

        # Check if we need to decrypt
        if (num_rails == 1):
            return message
        
        else:
            parts = ["" for m in message]
            k = 0
            for line in range(num_rails-1):
                skip = 2 * (num_rails - line - 1)
                j = 0
                i = line
                # Iterate through the message at interval equal to num rails
                while (i < len(message)):
                    parts[i] = message[k]
                    k += 1
                    if ((line == 0) or (j % 2 == 0)):
                        i += skip

                    else:
                        i += 2 * (num_rails - 1) - skip

                    j += 1

            # Get last line
            i = line + 1
            while (i < len(message)):
                parts[i] = message[k]
                k += 1
                i += 2 * (num_rails - 1)

            # Join the parts together
            output = "".join(parts)

            # Return the decrypted message
            return output

    def brute_force(self, message: str) -> str:
        """
        Function to decrypt the cipher using brute force
        """

        best_score = -99e9
        best_msg = ""
        # Try decrypting using 1-32 rails
        for key in range(1,33):
            # Get the shifted message
            curr_msg = self.with_key(message, key)

            # Get a score for that message
            curr_score = self.quadgram_scorer.ngram_score(curr_msg)

            # Check if score is better than previous best
            if (curr_score > best_score):
                # Update the best score and best message
                best_score = curr_score
                best_msg = curr_msg

        # Return the highest scoring message
        return best_msg