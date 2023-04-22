from utils.cipher_solver import CipherSolver

class RailfenceSolver(CipherSolver):

    """
    Class for decrypting ciphertexts encrypted using the Caesar cipher
    """

    def __init__(self) -> None:
        super().__init__()

    def with_key(self, message: str, key: int) -> str:
        if (key == 1):
            return message
        else:
            pt = ["" for i in range(len(message))]
            k=0
            for line in range(key-1):
                skip=2*(key-line-1)
                j=0
                i=line
                while (i<len(message)):
                    pt[i] = message[k]
                    k+=1
                    if ((line==0) or (j%2 == 0)):
                        i+=skip
                    else:
                        i+=2*(key-1) - skip  
                    j+=1       

            i=line+1  
            while (i<len(message)):
                pt[i] = message[k]
                k+=1
                i+=2*(key-1)

            output = "".join(pt)

            return output

    def brute_force(self, message: str) -> str:
        best_score = -99e9
        best_msg = ""
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

        return best_msg