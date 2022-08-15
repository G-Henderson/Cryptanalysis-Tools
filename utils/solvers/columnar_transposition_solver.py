from utils.cipher_solver import CipherSolver

class ColumnarTranspositionSolver(CipherSolver):

    """
    Class for decrypting ciphertexts encrypted using the Columnar Transposition cipher
    """

    def __init__(self) -> None:
        super().__init__()

    def with_key(self, message: str, key: str) -> str:
        # Setup grid
        grid = self.create_grid(message, key)

        # Put key into list
        key_as_list = list(key.upper())

        # Put key into alphabetical order
        sorted_list = sorted(key_as_list)

        output = ""
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                output += grid[i][sorted_list.index(key_as_list[j])]

        # Return the rearranged message
        return output

    def with_keylen(self, message: str, keylen: int) -> str:
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
        best_message = ""
        best_score = -99e9
        for keylen in range(2,10):
            # Get the best message using that keylen
            decrypt = self.with_keylen(message, keylen)
            # Get the score for the new decrypt
            current_score = self.quadgram_scorer.ngram_score(decrypt)

            # See if we have a new best score
            if (current_score > best_score):
                # Set the new best score and the new best message
                best_score = current_score
                best_message = decrypt

        # Return the best message
        return best_message

    def create_grid(self, message: str, key: str) -> list:
        # Put key into list
        key_as_list = list(key.upper())

        # Put key into alphabetical order
        sorted_list = sorted(key_as_list)

        # Get the number of columns and rows
        num_cols = len(key)
        num_rows = len(message) // num_cols
        # Check whether there's an overflow
        if ((len(message) % num_cols) > 0):
            # Add another row
            num_rows += 1

        # Create grid variable
        grid = [[""for col in range (num_cols)]for row in range (num_rows)]

        # Get the number of empty slots
        empty_slots = (num_cols * num_rows) - len(message)

        # Get the indexes of the empty rows
        cols_with_space = []
        for i in range(empty_slots):
            curr_index = -(i+1) # Get the index of the column that is going to have an empty space
            new_index = sorted_list.index(key_as_list[curr_index]) # Get the index of the column that currently has an empty space
            cols_with_space.append(new_index) # Add that to the list

        index = 0 # Keeps track of which letter we are at in the ciphertext
        for i in range(num_cols):
            # Check whether the column we are filling should have an empty space
            if (i in cols_with_space): remove = 1
            else: remove = 0

            # Iterate through the rows
            for j in range(num_rows-remove):
                # Add the current ciphertext letter to the grid
                grid[j][i] += message[index]
                # Add one to the ciphertext letter index
                index += 1

        # Return the grid variable
        return grid

    def get_permutations(self, list_digits: list) -> list:
        """
        Function to find all permutations of a string (that has been converted to a list)
        """

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