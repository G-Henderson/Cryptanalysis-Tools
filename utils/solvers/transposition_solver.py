from utils.cipher_solver import CipherSolver

class TranspositionSolver(CipherSolver):

    """
    Class for decrypting ciphertexts encrypted using the Transposition cipher
    """

    def __init__(self) -> None:
        # Initialise the super class
        super().__init__()

    def with_key(self, message: str, key: str) -> str:
        """
        Function for decrypting ciphertext from known key
        """

        # Setup empty variable to store the output
        output = ""

        # Iterate through the message at intervals of the key length
        for i in range(0, len(message), len(key)):
            # Get the current substring of key length characters
            sub_string = message[i:i+len(key)]
            # Iterate through the key
            for char in key:
                # Add the characters from the substring to the output
                # in the key order
                try:
                    # Try using digits
                    current_index = int(char)
                    try:
                        output += sub_string[current_index]
                    except:
                        pass
                except:
                    # Try using letters
                    ALPHABET = sorted(list(key))
                    current_index = ALPHABET.index(char)
                    try:
                        output += sub_string[current_index]
                    except:
                        pass

        # Return the rearranged message
        return output

    def with_keylen(self, message: str, keylen: int) -> str:
        """
        Function for decrypting ciphertext from known key length
        """

        # Get the number of digits needed for the key
        my_digits = [str(i) for i in range(keylen)]

        # Get the permutations of those digits
        my_permutations = self.get_permutations(my_digits)

        # Create variables to store the highest score and best permutation
        best_score = -99e9
        best_permutation = ""

        # Try all of the permutations
        for perm in my_permutations:
            # Convert the permutation to a string
            current_permutation = "".join(perm)
            # Decrypt using that permutation
            decrypt = self.with_key(message, current_permutation)
            # Score the decryption
            current_score = self.quadgram_scorer.ngram_score(decrypt)

            # Check if it is a new best score
            if (current_score > best_score):
                # Replace the best score and best permutation
                best_score = current_score
                best_permutation = current_permutation

        # Decrypt the message using the best permutation
        decrypt = self.with_key(message, best_permutation)

        # Return the decrypted message
        return decrypt

    def brute_force(self, message: str) -> str:
        """
        Function for decrypting ciphertext from known key
        """

        # Setup empty variable to store the best scoring message
        best_message = ""
        # Setup really low score as benchmark
        best_score = -99e9
        # Insert a new line
        print("")

        # Iterate through key lengths between 2 and 8
        for keylen in range(2,9):
            # Get the best message using that keylen
            decrypt = self.with_keylen(message, keylen)
            # Get the score for the new decrypt
            current_score = self.quadgram_scorer.ngram_score(decrypt)

            # Print message to show progress
            print(f"Key length: {keylen}, Score: {current_score}, Decrypt: {decrypt[:30]}...")

            # See if we have a new best score
            if (current_score > best_score):
                # Set the new best score and the new best message
                best_score = current_score
                best_message = decrypt

        # Return the best message
        return best_message