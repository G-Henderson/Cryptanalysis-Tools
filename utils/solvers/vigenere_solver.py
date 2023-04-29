from utils.ngrams_scorer import NgramScorer, NgramFiles
from utils.cipher_solver import CipherSolver

# Create class for storing top 100 keys
class BestList(object):

    """
    A list to store the top 100 keys 
    """

    def __init__(self) -> None:
        self.my_list = []
        self.max_len = 100

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

# Main class
class VigenereSolver(CipherSolver):

    """
    Class for decrypting ciphertexts encrypted using the Vigenere cipher
    """

    def __init__(self) -> None:
        # Initialise the super class
        super().__init__()

        # Setup trigram scorer instances
        self.trigram_scorer = NgramScorer(NgramFiles.TRIGRAM_FILE)

        # Setup the alphabet as a final variable
        self.ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def with_key(self, message: str, key: str) -> str:
        """
        Function for decrypting ciphertext from known key
        """

        # Initialise the variable to store the decrypted text
        decrypt = ""

        # Make sure the key is all caps
        key = key.upper()

        # Iterate through each character of the ciphertext
        for count, char in enumerate(message):
            decrypt += chr((((ord(char) - 65) - (ord(key[count % len(key)]) - 65) + 26) % 26) + 65)

        # Return the decrypted text
        return decrypt

    def with_keylen(self, message: str, keylen: int) -> str:
        """
        Function for decrypting ciphertext from known key length
        """

        # Create a best list
        best_list = BestList()

        # Find first 3 letters of key using permutations
        for perm in self.get_permutations(list(self.ALPHABET), 3):
            # Get the current key and pad with A's to make right keylen
            temp_key = ''.join(perm) + 'A' * (keylen - len(perm))
            # Try decrypting the with current key
            temp_decrypt = self.with_key(message, temp_key)
            # Get the fitness of the decrypted message using trigrams
            score = 0
            for i in range(0, len(message), keylen):
                score += self.trigram_scorer.ngram_score(temp_decrypt[i:i+3])

            # Add the score and key to the best list
            best_list.add((score, "".join(perm)))

        next_best_list = BestList()
        # Try finding the rest of the key
        for i in range(0, keylen-3):
            for k in range(100):
                for m in self.ALPHABET:
                    key = best_list[k][1] + m
                    full_key = key + 'A' * (keylen - len(key))
                    decrypt = self.with_key(message, full_key)

                    score = 0
                    for j in range(0, len(message), keylen):
                        score += self.quadgram_scorer.ngram_score(decrypt[j:j+len(key)])

                    next_best_list.add((score, key, decrypt[:30]))

            # Overwrite the old best list
            best_list = next_best_list
            # Reset the new one
            next_best_list = BestList()

        # Get the first key from the best list as the parent
        best_key = best_list[0][1]
        # Decrypt with the first key
        decrypt = self.with_key(message, best_key)
        # Get the benchmark score by using the first decrypt
        best_score = self.quadgram_scorer.ngram_score(decrypt)
        # Try the top 100 best keys
        for i in range(100):
            # Decrypt the ciphertext with the current key
            decrypt = self.with_key(message, best_list[i][1])
            # Score the new decrypt message using quadgrams
            score = self.quadgram_scorer.ngram_score(decrypt)
            # Check if we have a new highest score
            if score > best_score:
                # Replace the best key and set the new highest score
                best_key = best_list[i][1]
                best_score = score

        # Print the best key for that length
        print(f"\nBest key of length {len(best_key)} was '{best_key}'.")

        # Return the decrypted message
        return self.with_key(message, best_key)

    def brute_force(self, message: str) -> str:
        """
        Function for decrypting ciphertext using brute force
        """

        # Setup variables to store the best key length
        # and highest score
        best_keylen = 0
        best_score = -99e9

        # Try key lengths of 3 up to 10
        for keylen in range(3, 11):
            # Decrypt using the current key length
            decrypt = self.with_keylen(message, keylen)
            # Score the current decrypt
            score = self.quadgram_scorer.ngram_score(decrypt)

            # Display progress message
            print(f"Key length: {keylen}, Score: {score}, Decrypt: {decrypt[:30]}...")

            # Check if it is a new highscore
            if (score > best_score):
                # Replace the best score and best key length
                best_score = score
                best_keylen = keylen

        # Decrypt using the best key length
        decrypt = self.with_keylen(message, best_keylen)

        # Return the decrypt
        return decrypt

    def get_permutations(self, characters, permutation_length: int=None) -> list:
        """
        Generates permutations of a specific length using the list of characters specified
        """

        # Create list to store permutations in
        my_permutations = []
        
        # Check the permutation length
        num_chars = len(characters)
        if (permutation_length == None):
            permutation_length = num_chars
        
        indices = [i for i in range(num_chars)]
        cycles = [i for i in range(num_chars, num_chars-permutation_length, -1)]
        
        my_permutations.append([characters[i] for i in indices[:permutation_length]])
        
        while num_chars:
            for i in range(permutation_length-1, -1, -1):
                cycles[i] -= 1
                
                if cycles[i] == 0:
                    indices[i:] = indices[i+1:] + indices[i:i+1]
                    cycles[i] = num_chars - i
                    
                else:
                    j = cycles[i]
                    indices[i], indices[-j] = indices[-j], indices[i]
                    
                    my_permutations.append([characters[i] for i in indices[:permutation_length]])
                    
                    break
            
            else:
                # Return the permutations
                return my_permutations