from utils.cipher_solver import CipherSolver

class PlayfairSolver(CipherSolver):

    """
    Class for decrypting ciphertexts encrypted using the Playfair cipher
    """

    def __init__(self) -> None:
        super().__init__()
        
    def with_key(self, message: str, key_table: list) -> str:
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
    
    def split_into_pairs(self, message: str) -> list:
        """
        Function to split the text into list containing pairs of letters
        """

        pairs = []
        start_index = 0

        for end_index in range(2, len(message), 2):
            pairs.append(message[start_index:end_index])
            start_index = end_index

        pairs.append(message[start_index:])

        return pairs
    
    def double_char(self, text: str) -> str:
        """
        Function to fill string if there are two of the same letters in a string
        """

        # Check whether the length of text is odd or even
        len_txt = len(text)
        is_odd = 0
        if not (len_txt % 2) == 0:
            is_odd = 1

        for i in range(0, len_txt-is_odd, 2):
            if (text[i] == text[i+1]):
                new_text = f"{text[0:i+1]}x{text[i+1:]}"
                new_text = self.double_char(new_text)
                break

            else:
                new_text = text

        return new_text